import json
import scrapy
from jobs_project.items import JobItem

class JobSpider(scrapy.Spider):
    name = 'job_spider'
    custom_settings = {
        'ITEM_PIPELINES': {
            'jobs_project.pipelines.PostgreSQLPipeline': 300,
        }
    }

    def start_requests(self):
        for filename in ['sample.json', 'sample2.json']:
            yield scrapy.Request(
                url=f'file:///jobs_project/{filename}',
                callback=self.parse_page,
            )

    def parse_page(self, response):
        jobs = json.loads(response.body)

        for job in jobs.get('jobs', []):
            item = JobItem()
            job_data = job.get('data', {})

            fields = [
                'slug', 'language', 'languages', 'req_id', 'title', 'description',
                'location_name', 'street_address', 'city', 'state', 'country',
                'country_code', 'postal_code', 'location_type', 'latitude',
                'longitude', 'categories', 'tags', 'tags5', 'tags6', 'brand',
                'promotion_value', 'salary_currency', 'salary_value',
                'salary_min_value', 'salary_max_value', 'benefits',
                'employment_type', 'hiring_organization', 'source', 'apply_url',
                'internal', 'searchable', 'applyable', 'li_easy_applyable',
                'ats_code', 'meta_data', 'update_date', 'create_date', 'category',
                'full_location', 'short_location'
            ]
            for field in fields:
                item[field] = job_data.get(field)
            
            yield item
