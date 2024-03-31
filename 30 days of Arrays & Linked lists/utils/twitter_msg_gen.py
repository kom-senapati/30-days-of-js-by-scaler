from random import choice

message_templates = [
    "🌟 Completed Day # of 30 Days of arrays & linked lists challenge on Scaler Discord! 🚀 Let's celebrate!",
    "🎉 Conquered Day # of 30 Days of arrays & linked lists on Scaler Discord! 💪 Ready for more?",
    "🚀 Another triumph! Day # of 30 Days of arrays & linked lists challenge on Scaler Discord done! 🌟 Keep coding!",
    "💡 Navigated Day # of 30 Days of arrays & linked lists challenge on Scaler Discord! 🌈 Let's keep the momentum!",
    "🎊 Triumphed Day # of 30 Days of arrays & linked lists challenge on Scaler Discord! 💻 Ready for more?",
    "🌈 Milestone achieved! Day # of 30 Days of arrays & linked lists challenge on Scaler Discord conquered! 🎉 Let's code!",
    "👏 Day # of 30 Days of arrays & linked lists challenge on Scaler Discord completed successfully! 🚀 Keep pushing limits!",
    "💪 Finished Day # of 30 Days of arrays & linked lists challenge on Scaler Discord! 🌟 Keep coding & exploring!",
    "🎉 Successfully completed Day # of 30 Days of arrays & linked lists challenge on Scaler Discord! 🚀 Join me for more!",
]

day = input("Day > ")
print()
print("Copy and post on Twitter 👇\n")
print(
    choice(message_templates).replace("#", day)
    + "\nJoin the adventure, tackle challenges, and connect with enthusiasts! https://bit.ly/scalerdiscord\n#30DaysOfNodejs #ScalerDiscord #ScalerTopics @scaler_official"
)
