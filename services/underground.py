from settings import REGIONS_WITH_UNDERGROUNDS


def is_underground_exists(region_id: int) -> bool:
    return region_id in REGIONS_WITH_UNDERGROUNDS

