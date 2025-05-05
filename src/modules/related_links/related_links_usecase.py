from src.modules.related_links.related_links_viewmodel import RelatedLinksViewModel
from src.modules.related_links.related_links_repository import RelatedLinksRepository

class RelatedLinksUseCase:
    def __init__(self, repo: RelatedLinksRepository):
        self.repo = repo

    def __call__(self, data: dict):
        try:
            resume = data.get("resume")
            if not resume:
                raise Exception("Resume not found in token")
            
            output = self.repo.rate_site_relevance(site_url=data.get("site_url"), user_resume=resume)
            score_and_text = RelatedLinksViewModel(
                text=output['explicacao'],
                score=output['nota']
            ).dict()
            return score_and_text
        except Exception as e:
            raise Exception(f"{str(e)}")
