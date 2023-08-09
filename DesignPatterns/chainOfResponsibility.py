# behavioral design pattern that lets you pass request along a chain of handlers
# each handler may either process a part of request
# or simply pass along the request and only one processes the request

from __future__ import annotations
from abc import ABC, abstractmethod


class Issue:
    def __init__(self, description, severity: int) -> None:
        self.description = description
        self.severity = severity


class AbstractHandler(ABC):
    def __init__(self, next: AbstractHandler) -> None:
        self.next = next

    def handle(self, issue: Issue):
        handled = self.processIssue(issue)

        if not handled:
            if self.next:
                self.next.handle(issue)
            else:
                print(f"No one able to handle this issue: {issue.description}")

    @abstractmethod
    def processIssue(self, issue: Issue) -> bool:
        pass


class LocalOfficer(AbstractHandler):
    def __init__(self, next: AbstractHandler, maxSeverity: int) -> None:
        self.next = next
        self.maxSeverity = maxSeverity

    def processIssue(self, issue: Issue) -> bool:
        if issue.severity <= self.maxSeverity:
            print(f"Local officer handled the issue: {issue.description}")
            return True


class DistrictOfficer(AbstractHandler):
    def __init__(self, next: AbstractHandler, maxSeverity: int) -> None:
        self.next = next
        self.maxSeverity = maxSeverity

    def processIssue(self, issue: Issue) -> bool:
        if issue.severity <= self.maxSeverity:
            print(f"DistrictOfficer handled the issue: {issue.description}")
            return True


class StateOfficer(AbstractHandler):
    def __init__(self, next: AbstractHandler, maxSeverity: int) -> None:
        self.next = next
        self.maxSeverity = maxSeverity

    def processIssue(self, issue: Issue) -> bool:
        if issue.severity <= self.maxSeverity:
            print(f"State Officer handled the issue: {issue.description}")
            return True


if __name__ == "__main__":
    stateOfficer = StateOfficer(None, 10)
    districtOfficer = DistrictOfficer(stateOfficer, 5)
    localOfficer = LocalOfficer(districtOfficer, 2)

    issues = [
        Issue("House Plumbing Issue", 1),
        Issue("Power Outage", 3),
        Issue("Floods", 9),
        Issue("Terrorist Attack", 12),
    ]

    for issue in issues:
        localOfficer.handle(issue)
        print("-" * 10)
