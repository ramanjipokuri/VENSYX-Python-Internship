class InsightGenerator:

    def generate(self, avg_time, category, risky_count):
        return f"""
--- Digital Footprint Insights ---
 Average daily screen time: {avg_time} minutes
 High {category} usage
 Risky site visits: {risky_count}
"""
