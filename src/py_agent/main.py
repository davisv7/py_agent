from py_agent.agent import Agent

from py_agent.jobs import github_notifications
from py_agent.listeners import add_issue_to_todoist, add_pr_to_todoist

agent = Agent()

agent.schedule.every(10).minutes.do(github_notifications, handler=agent.handler)

agent.add_listener(add_issue_to_todoist, {'event_type': ('==', 'new_issue_assigned')})
agent.add_listener(add_pr_to_todoist, {'event_type': ('==', 'new_pr_review')})

agent.go()