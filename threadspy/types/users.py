from typing import List
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from threadspy.types.threads_user import ThreadsUser


@dataclass_json
@dataclass
class UsersData:
    users: List[ThreadsUser]
