from dataclasses import dataclass
from ..enums import AnixartLists, AnixartReleaseStatus, AnixartReleaseCategory, AnixartReleaseAgeRating, AnixartReleaseSeason

@dataclass
class Release:
    title_original: str
    title_ru: str
    title_alt: str
    description: str
    author: str
    director: str
    studio: str
    image_url: str
    country: str
    translators: str
    year: str
    genres: str
    rating: int
    grade: float
    status: AnixartReleaseStatus
    category: AnixartReleaseCategory
    season: AnixartReleaseSeason
    release_date: str
    creation_date: int
    last_update_date: int
    related: ReleaseRelated
    age_rating: AnixartReleaseAgeRating
    duration: int # минуты
    broadcast: int # день недели [1-7]
    aired_on_date: int
    profile_release_type_notification_preference_count: int
    vote1_count: int
    vote2_count: int
    vote3_count: int
    vote4_count: int
    vote5_count: int
    vote_count: int
    your_vote: int
    voted_date: int
    my_vote: int # [1-5]
    episodes_total: int
    collection_count: int
    favorite_count: int
    comment_count: int
    comment_per_day_count: int
    watched_count: int
    dropped_count: int
    hold_on_count: int
    plan_count: int
    watching_count: int
    episode_last_update: EpisodeUpdate
    episodes_released: int
    last_set_completed_date: int
    last_set_dropped_date: int
    last_set_favorite_date: int
    last_set_hold_on_date: int
    last_set_plan_date: int
    last_set_viewed_date: int
    last_set_watching_date: int
    last_view_date: int
    last_view_episode: Episode
    last_view_episode_name: str
    last_view_episode_type_name: str
    note: str
    profile_list_status: AnixartLists
    is_adult: bool
    is_deleted: bool
    is_favorite: bool
    is_viewed: bool
    is_play_disabled: bool
    is_release_type_notifications_enabled: bool
    is_third_party_platforms_disabled: bool
    is_view_blocked: bool
    can_torlook_search: bool
    can_video_appeal: bool