from django.core.paginator import Paginator

class OddPaginator(Paginator):
    def leading_page_range(self, page_number=1, display_count=3):
        return range(1, min(self.current_page_range(page_number=page_number)[0], display_count + 1))

    def current_page_range(self, page_number=1, display_count=4):
        return range(max(page_number - display_count, 1), min(page_number + display_count, self.num_pages + 1))

    def trailing_page_range(self, page_number=1, display_count=3):
        return range(max(self.num_pages - display_count + 1, self.current_page_range(page_number=page_number)[-1] + 1), self.num_pages + 1)
