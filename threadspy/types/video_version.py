from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class VideoVersion:
    type: int
    url: str
    # __typename: str