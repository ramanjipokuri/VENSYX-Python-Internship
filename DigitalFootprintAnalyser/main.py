from utils.file_readers import read_screen_time, read_app_usage
from utils.docstream import stream_browsing_file
from core.analyzer import DigitalFootprintAnalyzer
from core.insights import InsightGenerator
from core.cache import get_cached_report, set_cached_report

WEEK = "week1"

def main():
    cached = get_cached_report(WEEK)
    if cached:
        print(cached)
        return

    screen_time = read_screen_time(f"data/{WEEK}/screen_time.csv")
    app_usage = read_app_usage(f"data/{WEEK}/app_usage.csv")
    browsing = stream_browsing_file(f"data/{WEEK}/browsing.txt")

    analyzer = DigitalFootprintAnalyzer()
    insights = InsightGenerator()

    avg_time = analyzer.average_screen_time(screen_time)
    category = analyzer.dominant_category(app_usage)
    risky_count = analyzer.count_risky_sites(browsing)

    report = insights.generate(avg_time, category, risky_count)
    set_cached_report(WEEK, report)

    print(report)

if __name__ == "__main__":
    main()
