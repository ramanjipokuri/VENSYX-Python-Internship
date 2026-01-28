_cache = {}

def get_cached_report(week):
    return _cache.get(week)

def set_cached_report(week, report):
    _cache[week] = report
