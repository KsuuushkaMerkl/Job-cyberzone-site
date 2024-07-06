from uuid import UUID

from core.schemas import Schemas


photo_url = {
    "COSPLAY": "https://s3.cyberzone.dev/job-site-assets/cosplay.png",
    "CRAFT": "https://s3.cyberzone.dev/job-site-assets/craft.png",
    "DESIGN": "https://s3.cyberzone.dev/job-site-assets/design.png",
    "IT": "https://s3.cyberzone.dev/job-site-assets/it.png",
    "PHOTO": "https://s3.cyberzone.dev/job-site-assets/photo.png",
    "CYBERSPORT":  "https://s3.cyberzone.dev/job-site-assets/cybersport.png",
    "SMM":  "https://s3.cyberzone.dev/job-site-assets/smm.png",
    "TABLEGAMES": "https://s3.cyberzone.dev/job-site-assets/tablegames.png",
    "TWITCH": "https://s3.cyberzone.dev/job-site-assets/twitch.png",
    "VIDEO": "https://s3.cyberzone.dev/job-site-assets/video.png"
}

logo_url = {
    "COSPLAY": "https://s3.cyberzone.dev/job-site-assets/cosplay_logo.png",
    "CRAFT": "https://s3.cyberzone.dev/job-site-assets/craft_logo.png",
    "DESIGN": "https://s3.cyberzone.dev/job-site-assets/design_logo.png",
    "IT": "https://s3.cyberzone.dev/job-site-assets/it_logo.png",
    "PHOTO": "https://s3.cyberzone.dev/job-site-assets/photo_logo.png",
    "CYBERSPORT":  "https://s3.cyberzone.dev/job-site-assets/cybersport_logo.png",
    "SMM":  "https://s3.cyberzone.dev/job-site-assets/smm_logo.png",
    "TABLEGAMES": "https://s3.cyberzone.dev/job-site-assets/tablegames_logo.png",
    "TWITCH": "https://s3.cyberzone.dev/job-site-assets/twitch_logo.png",
    "VIDEO": "https://s3.cyberzone.dev/job-site-assets/video_logo.png"
}


class VacancySchema(Schemas):
    """
    Vacancy schema
    """
    id: UUID
    name: str
    department: str
    photo_url: str | None = None
    logo_url: str | None = None
    level: str
    location: str
    important: bool
    requirements: list[str]
    tasks: list[str]
    task: str


class VacancyIdSchema(Schemas):
    """
    Vacancy schema
    """
    id: UUID
    name: str
    department: str
    photo_url: str | None = None
    logo_url: str | None = None
    level: str
    location: str
    info: str
    requirements: list[str]
    tasks: list[str]
    task: str


class CreateVacancyRequestSchema(Schemas):
    """
    Create vacancy request schema
    """ 
    name: str
    department: str
    level: str
    location: str
    important: bool
    info: str
    requirements: list[str]
    tasks: list[str]
    task: str


class UpdateVacancyRequestSchema(Schemas):
    """
    Update vacancy request schema
    """
    name: str | None = None
    department: str | None = None
    photo_url: str | None = None
    logo_url: str | None = None
    level: str | None = None
    location: str | None = None
    important: bool | None = None
    info: str | None = None
    requirements: list[str] | None = None
    tasks: list[str] | None = None
    task: str | None = None


