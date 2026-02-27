from data_loader import run_query
import queries


def insight_1_customer_profile():
    df = run_query(queries.INSIGHT_1)
    return df


def insight_2_search_behavior():
    df = run_query(queries.INSIGHT_2)
    return df


def insight_3_location_activity():
    df = run_query(queries.INSIGHT_3)
    return df


def insight_4_property_performance():
    df = run_query(queries.INSIGHT_4)
    return df


def insight_5_funnel_analysis():

    df = run_query(queries.INSIGHT_5)

    # conversion calculations
    df["wishlist_rate"] = df["wishlists"] / df["searches"]
    df["visit_rate"] = df["visits"] / df["wishlists"]
    df["contact_rate"] = df["contacts"] / df["visits"]

    return df

def insight_city_funnel():

    df = run_query(queries.INSIGHT_CITY_FUNNEL)

    # conversion calculations
    df["wishlist_rate"] = df["wishlists"] / df["searches"]
    df["visit_rate"] = df["visits"] / df["wishlists"]
    df["contact_rate"] = df["contacts"] / df["visits"]

    return df


def insight_property_type_funnel():

    df = run_query(queries.INSIGHT_PROPERTY_TYPE_FUNNEL)

    df["wishlist_rate"] = df["wishlists"] / df["searches"]
    df["visit_rate"] = df["visits"] / df["wishlists"]
    df["contact_rate"] = df["contacts"] / df["visits"]

    return df

def insight_occupation_funnel():
    """
    Occupation based funnel analysis
    """

    # Step 1 — execute SQL
    df = run_query(queries.INSIGHT_OCCUPATION_FUNNEL)

    # Step 2 — conversion metrics
    df["wishlist_rate"] = df["wishlists"] / df["searches"]

    df["visit_rate"] = df["visits"] / df["wishlists"]

    df["contact_rate"] = df["contacts"] / df["visits"]

    # Step 3 — sort by strongest conversion
    df = df.sort_values("contact_rate", ascending=False)

    return df