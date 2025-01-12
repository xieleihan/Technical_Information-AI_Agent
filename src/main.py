# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at <https://www.jetbrains.com/help/pycharm/>

from config import Config
from scheduler import Scheduler
from github_client import GitHubClient
from notifier import Notifier
from report_generator import ReportGenerator
from subscription_manager import SubscriptionManager

def main():
    config = Config()
    github_client = GitHubClient(config.github_token)
    notifier = Notifier(config.notification_settings)
    report_generator = ReportGenerator()
    subscription_manager = SubscriptionManager(config.subscriptions_file)

    scheduler = Scheduler(
        github_client=github_client,
        notifier=notifier,
        report_generator=report_generator,
        subscription_manager=subscription_manager,
        interval=config.update_interval
    )

    scheduler.start()

if __name__ == "__main__":
    main()
