from scrapy.item import Item, Field

class JobItem(Item):
    slug = Field()
    language = Field()
    languages = Field()
    req_id = Field()
    title = Field()
    description = Field()
    location_name = Field()
    street_address = Field()
    city = Field()
    state = Field()
    country = Field()
    country_code = Field()
    postal_code = Field()
    location_type = Field()
    latitude = Field()
    longitude = Field()
    categories = Field()
    tags = Field()
    tags5 = Field()
    tags6 = Field()
    brand = Field()
    promotion_value = Field()
    salary_currency = Field()
    salary_value = Field()
    salary_min_value = Field()
    salary_max_value = Field()
    benefits = Field()
    employment_type = Field()
    hiring_organization = Field()
    source = Field()
    apply_url = Field()
    internal = Field()
    searchable = Field()
    applyable = Field()
    li_easy_applyable = Field()
    ats_code = Field()
    meta_data = Field()
    update_date = Field()
    create_date = Field()
    category = Field()
    full_location = Field()
    short_location = Field()
