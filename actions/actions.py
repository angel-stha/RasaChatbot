# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import requests
from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class GetTodaysCases(Action):
    """
        A class fetches API for the new cases of covid from
        https://corona.askbhunte.com/api/v1/data/nepal

            ...
                Attributes
                ----------
                takes own self attributes of rasa action

                Methods
                -------
                run():
                    returns the dispatcher that sends message
                    back to user,tracker the state
                    tracker for the current user and domain

    """
    def name(self):

        """
            Constructs all the necessary attributes for the Action.

                Returns
                ----------
                name of the action that is used by the bot upon intent
        """
        return "get_todays_cases"

    def run(self, dispatcher, tracker, domain):
        """
            Returns the response message as for utter in the
            name of the action above.
                Parameters
                ----------
                dispatcher: text
                            message to be displace to user by bot.
                tracker: state of tracker for current user
                domain: is the representation of domain.yml file.
                Returns
                ----------
                response(text): the information extracted from the API
                                for this custom ction.

        """

        url = 'https://corona.askbhunte.com/api/v1/data/nepal'

        res = requests.get(url)
        todays_positive = res.json()['tested_positive']
        negative = res.json()['tested_negative']
        response = "Cases in 2020-10-20:\n{}".format(todays_positive)
        dispatcher.utter_message(response)
        return (response)