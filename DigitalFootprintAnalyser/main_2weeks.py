import sys
import os
from utils.file_readers import read_screen_time, read_app_usage
from utils.docstream import stream_browsing_file
from core.analyzer import DigitalFootprintAnalyzer
from core.insights import InsightGenerator
from core.cache import get_cached_report, set_cached_report


def get_all_weeks(data_dir="data"):
    """
    Auto-detect week folders inside data/
    Example: week1, week2, week3 ...
    """
    weeks = []
    for name in os.listdir(data_dir):
        path = os.path.join(data_dir, name)
        if os.path.isdir(path) and name.lower().startswith("week"):
            weeks.append(name)

    return sorted(weeks)


def analyze_week(week):
    # ---------- CACHE CHECK ----------
    cached = get_cached_report(week)
    if cached:
        print(f"(From Cache) {week}")
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

    # ---------- CACHE ----------
    set_cached_report(week, report)

    print(f"(Computed) {week}")
    print(report)


def main():
    # ---------- WEEK SELECTION ----------
    if len(sys.argv) > 1:
        weeks = sys.argv[1:]
        mode = "Manual"
    else:
        weeks = get_all_weeks()
        mode = "Auto-detected"

    print("=== Digital Footprint Analysis ===")
    print(f"Mode: {mode}\n")

    if not weeks:
        print("No week data found inside data/ folder.")
        return

    for week in weeks:
        analyze_week(week)
        print("-" * 40)


if __name__ == "__main__":
    main()
