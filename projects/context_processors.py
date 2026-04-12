from .models import Profile, SocialLink, Skill, Experience, Education, Service


def portfolio_context(request):
    try:
        return {
            'profile': Profile.objects.first(),
            'social_links': SocialLink.objects.filter(is_active=True) if hasattr(SocialLink, 'is_active') else [],
            'skills': Skill.objects.filter(is_active=True) if hasattr(Skill, 'is_active') else [],
            'experiences': Experience.objects.filter(is_active=True) if hasattr(Experience, 'is_active') else [],
            'education': Education.objects.filter(is_active=True) if hasattr(Education, 'is_active') else [],
            'services': Service.objects.filter(is_active=True) if hasattr(Service, 'is_active') else [],
        }
    except Exception:
        return {}
