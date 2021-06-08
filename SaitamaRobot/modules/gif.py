import TenGiphPy

from SaitamaRobot import dispatcher

from SaitamaRobot.modules.disable import DisableAbleCommandHandler

from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update, InlineQueryResultGif

from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext, run_async

from uuid import uuid4

@run_async

def giphy(update: Update, _: CallbackContext) -> None:

    query = update.inline_query.query

    if query == '':

        return

    else:   

        if query.startswith('.gif '):    

            query = query.replace('.gif ','')

            client = TenGiphPy.Tenor(token='XLAX67BXI3S7')

            

            try: 

                search = client.search(query,limit=50)

                if not search:

                    return

                if not search['results']:

                    return

                urls = []

                for gif in search['results']:

                    urls.append(gif['url'])

                results = [

                    InlineQueryResultGif(

                        id=str(uuid4()),

                        gif_url=url,

                        thumb_url=url

                    ) for url in urls

                ]

                update.inline_query.answer(results,cache_time=1)

            except ApiException as e:

                results = [

                    InlineQueryResultArticle(

                        id=str(uuid4()),

                        title='404 Not Founmd',

                        input_message_content=InputTextMessageContent('Try Some Other Query ')

                    )

                ]

                update.inline_query.answer(results,cache_time=1)

        else:   

            results = [

                InlineQueryResultArticle(

                    id=str(uuid4()),

                    title='Loamding Pleamse Waimt...',

                    input_message_content=InputTextMessageContent('Seamrching...')

                )

            ]

            update.inline_query.answer(results,cache_time=1)

dispatcher.add_handler(InlineQueryHandler(giphy))
