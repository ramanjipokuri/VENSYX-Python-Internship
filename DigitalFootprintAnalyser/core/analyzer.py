from collections import defaultdict

RISKY_SITES = {"youtube.com", "facebook.com", "snapchat.com", "tiktok.com"}

class DigitalFootprintAnalyzer:

    def average_screen_time(self, minutes):
        return round(sum(minutes) / len(minutes), 1)

    def dominant_category(self, app_usage):
        category_time = defaultdict(int)

        for row in app_usage:
            category_time[row["category"]] += row["minutes"]

        return max(category_time, key=category_time.get)

    def count_risky_sites(self, browsing_generator):
        return sum(1 for site in browsing_generator if site in RISKY_SITES)
