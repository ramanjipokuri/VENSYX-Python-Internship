import sys
from utils.file_readers import read_screen_time, read_app_usage
from utils.docstream import stream_browsing_file
from core.analyzer import DigitalFootprintAnalyzer
from core.insights import InsightGenerator
from core.cache import get_cached_report, set_cached_report


def main():
    # ---------- WEEK INPUT ----------
    if len(sys.argv) > 1:
        week = sys.argv[1]
    else:
        week = "week2"

    # ---------- CACHE CHECK ----------
    cached = get_cached_report(week)
    if cached:
        print(f"(From Cache) {week}\n")
        print(cached)
        return

    # ---------- DATA PATHS ----------
    screen_time_path = f"data/{week}/screen_time.csv"
    app_usage_path = f"data/{week}/app_usage.csv"
    browsing_path = f"data/{week}/browsing.txt"

    # ---------- READ DATA ----------
    screen_time = read_screen_time(screen_time_path)
    app_usage = read_app_usage(app_usage_path)
    browsing = stream_browsing_file(browsing_path)

    # ---------- ANALYSIS ----------
    analyzer = DigitalFootprintAnalyzer()
    insights = InsightGenerator()

    avg_time = analyzer.average_screen_time(screen_time)
    category = analyzer.dominant_category(app_usage)
    risky_count = analyzer.count_risky_sites(browsing)

    report = insights.generate(avg_time, category, risky_count)

    # ---------- CACHE RESULT ----------
    set_cached_report(week, report)

    print(f"(Computed) {week}\n")
    print(report)


if __name__ == "__main__":
    main()
