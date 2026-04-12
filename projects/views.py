from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Blog, Contact, Profile, SocialLink, Skill, Experience, Education, Service
from .forms import ContactForm


def get_portfolio_context():
    profile = Profile.objects.first()
    if profile is None:
        profile = type('Profile', (), {
            'name': 'Your Name',
            'title': 'Full Stack Developer',
            'subtitle': '',
            'email': '',
            'phone': '',
            'location': '',
            'about_title': '',
            'about_content': '',
            'hero_stats': {},
            'response_time': '',
            'seo_title': '',
            'seo_description': '',
            'seo_keywords': '',
        })()
    
    skills = Skill.objects.filter(is_active=True)
    if not skills.exists():
        skills = [
            type('Skill', (), {'name': 'Python', 'category': 'backend', 'icon_class': 'fab fa-python', 'proficiency': 90})(),
            type('Skill', (), {'name': 'Django', 'category': 'backend', 'icon_class': 'fas fa-server', 'proficiency': 85})(),
            type('Skill', (), {'name': 'JavaScript', 'category': 'frontend', 'icon_class': 'fab fa-js', 'proficiency': 85})(),
            type('Skill', (), {'name': 'React', 'category': 'frontend', 'icon_class': 'fab fa-react', 'proficiency': 80})(),
            type('Skill', (), {'name': 'PostgreSQL', 'category': 'database', 'icon_class': 'fas fa-database', 'proficiency': 85})(),
            type('Skill', (), {'name': 'Data Analysis', 'category': 'other', 'icon_class': 'fas fa-chart-line', 'proficiency': 85})(),
            type('Skill', (), {'name': 'Excel', 'category': 'other', 'icon_class': 'fas fa-file-excel', 'proficiency': 95})(),
            type('Skill', (), {'name': 'Power BI', 'category': 'other', 'icon_class': 'fas fa-chart-pie', 'proficiency': 85})(),
            type('Skill', (), {'name': 'Cybersecurity', 'category': 'other', 'icon_class': 'fas fa-shield-alt', 'proficiency': 75})(),
            type('Skill', (), {'name': 'Docker', 'category': 'devops', 'icon_class': 'fab fa-docker', 'proficiency': 80})(),
        ]
    
    services = Service.objects.filter(is_active=True)
    if not services.exists():
        services = [
            type('Service', (), {'title': 'Full Stack Development', 'description': 'End-to-end web application development with modern technologies.', 'icon_class': 'fas fa-code', 'icon_color': 'sky', 'features': ['Django & Flask', 'React & Next.js', 'RESTful APIs', 'Responsive Design']})(),
            type('Service', (), {'title': 'Data Analysis', 'description': 'Transform raw data into actionable insights for better decision-making.', 'icon_class': 'fas fa-chart-line', 'icon_color': 'purple', 'features': ['Python & Pandas', 'SQL & Excel', 'Data Visualization', 'Statistical Analysis']})(),
            type('Service', (), {'title': 'Microsoft Suite', 'description': 'Professional spreadsheet, presentation, and document solutions.', 'icon_class': 'fas fa-file-excel', 'icon_color': 'blue', 'features': ['Excel & Power BI', 'Word & PowerPoint', 'VBA Automation', 'Data Dashboards']})(),
            type('Service', (), {'title': 'Cybersecurity Analysis', 'description': 'Protect your digital assets with comprehensive security assessments.', 'icon_class': 'fas fa-shield-alt', 'icon_color': 'red', 'features': ['Vulnerability Assessment', 'Security Audits', 'Risk Analysis', 'Security Best Practices']})(),
            type('Service', (), {'title': 'Database Design', 'description': 'Efficient database architecture and optimization for scalable applications.', 'icon_class': 'fas fa-database', 'icon_color': 'emerald', 'features': ['PostgreSQL & MySQL', 'MongoDB', 'Redis Caching', 'Data Migration']})(),
            type('Service', (), {'title': 'Cloud & DevOps', 'description': 'Deployment, CI/CD, and cloud infrastructure management.', 'icon_class': 'fas fa-cloud', 'icon_color': 'orange', 'features': ['AWS & GCP', 'Docker & Kubernetes', 'CI/CD Pipelines', 'Monitoring']})(),
        ]
    
    return {
        'profile': profile,
        'social_links': SocialLink.objects.filter(is_active=True),
        'skills': skills,
        'experiences': Experience.objects.filter(is_active=True),
        'education': Education.objects.filter(is_active=True),
        'services': services,
    }


def get_default_blogs():
    now = timezone.now()
    return [
        type('Blog', (), {
            'title': 'Getting Started with Django Web Development',
            'slug': 'getting-started-with-django',
            'content': 'Django is a powerful Python web framework that enables rapid development of secure and maintainable websites. In this comprehensive guide, we will explore the fundamentals of Django and how to build your first web application.\n\n## Why Choose Django?\n\nDjango offers several advantages:\n\n- **Batteries Included**: Comes with built-in admin interface, authentication, and more\n- **Security**: Protects against common vulnerabilities like SQL injection and XSS\n- **Scalability**: Used by Instagram, Pinterest, and other high-traffic sites\n- **Community**: Large ecosystem of packages and excellent documentation\n\n## Setting Up Your First Project\n\n```python\npip install django\ndjango-admin startproject myproject\ncd myproject\npython manage.py runserver\n```\n\nThis creates a basic Django project that you can extend with your own applications.',
            'summary': 'Learn the fundamentals of Django web development and build your first web application with this comprehensive guide.',
            'author': 'Admin',
            'published_date': now - timezone.timedelta(days=3),
            'published': True,
            'featured': True,
            'views': 150,
            'get_absolute_url': lambda: '/blog/getting-started-with-django/',
        })(),
        type('Blog', (), {
            'title': 'Data Analysis with Python and Pandas',
            'slug': 'data-analysis-python-pandas',
            'content': 'Python has become the go-to language for data analysis, largely thanks to pandas - a powerful library for data manipulation and analysis. This article covers essential techniques for working with data.\n\n## Introduction to Pandas\n\nPandas provides two primary data structures:\n\n- **Series**: One-dimensional labeled array\n- **DataFrame**: Two-dimensional labeled data structure\n\n## Loading and Exploring Data\n\n```python\nimport pandas as pd\ndf = pd.read_csv("data.csv")\nprint(df.head())\nprint(df.describe())\n```\n\n## Data Cleaning Techniques\n\n- Handling missing values\n- Removing duplicates\n- Data type conversion\n- Feature engineering',
            'summary': 'Master data analysis with Python and Pandas. Learn essential techniques for loading, cleaning, and analyzing data effectively.',
            'author': 'Admin',
            'published_date': now - timezone.timedelta(days=7),
            'published': True,
            'featured': True,
            'views': 230,
            'get_absolute_url': lambda: '/blog/data-analysis-python-pandas/',
        })(),
        type('Blog', (), {
            'title': 'Cybersecurity Best Practices for Developers',
            'slug': 'cybersecurity-best-practices',
            'content': 'As developers, we must prioritize security in every application we build. This guide covers essential cybersecurity practices that every developer should know.\n\n## Common Vulnerabilities\n\n1. **SQL Injection**: Never concatenate user input into queries\n2. **XSS (Cross-Site Scripting)**: Always sanitize user input\n3. **CSRF**: Use Django\'s built-in CSRF protection\n4. **Password Storage**: Never store plain-text passwords\n\n## Security Checklist\n\n- [ ] Use HTTPS everywhere\n- [ ] Implement proper authentication\n- [ ] Validate and sanitize all inputs\n- [ ] Keep dependencies updated\n- [ ] Conduct regular security audits\n\n## Conclusion\n\nSecurity is not an afterthought - it must be built into every layer of your application from the start.',
            'summary': 'Essential cybersecurity practices every developer should implement to protect their applications from common vulnerabilities.',
            'author': 'Admin',
            'published_date': now - timezone.timedelta(days=12),
            'published': True,
            'featured': True,
            'views': 180,
            'get_absolute_url': lambda: '/blog/cybersecurity-best-practices/',
        })(),
        type('Blog', (), {
            'title': 'Mastering Microsoft Excel for Business Analytics',
            'slug': 'mastering-microsoft-excel',
            'content': 'Excel remains one of the most powerful tools for business analytics. This guide will take you from basic spreadsheet functions to advanced data analysis techniques.\n\n## Essential Functions\n\nLearn the most important functions like VLOOKUP, INDEX/MATCH, IF statements, and array formulas.\n\n## Pivot Tables\n\nMaster pivot tables to summarize and analyze large datasets quickly.\n\n## Data Visualization\n\nCreate impactful charts and dashboards that communicate insights effectively.',
            'summary': 'Transform your Excel skills from basic to advanced with these essential business analytics techniques.',
            'author': 'Admin',
            'published_date': now - timezone.timedelta(days=18),
            'published': True,
            'featured': True,
            'views': 320,
            'get_absolute_url': lambda: '/blog/mastering-microsoft-excel/',
        })(),
        type('Blog', (), {
            'title': 'Introduction to Power BI for Data Visualization',
            'slug': 'introduction-to-power-bi',
            'content': 'Power BI is Microsoft\'s powerful business intelligence tool for creating interactive dashboards and reports. Learn how to transform your data into actionable insights.\n\n## Getting Started\n\nConnect to various data sources and import your datasets into Power BI Desktop.\n\n## Data Modeling\n\nCreate relationships between tables and build efficient data models.\n\n## Visualizations\n\nBuild interactive reports with various chart types and custom visuals.',
            'summary': 'Learn how to create stunning interactive dashboards and reports with Microsoft Power BI.',
            'author': 'Admin',
            'published_date': now - timezone.timedelta(days=25),
            'published': True,
            'featured': True,
            'views': 275,
            'get_absolute_url': lambda: '/blog/introduction-to-power-bi/',
        })(),
        type('Blog', (), {
            'title': 'Building REST APIs with Django REST Framework',
            'slug': 'building-rest-apis-django',
            'content': 'Learn how to build robust and scalable REST APIs using Django REST Framework (DRF).\n\n## Setting Up DRF\n\nInstall and configure Django REST Framework in your Django project.\n\n## Serializers\n\nCreate serializers to convert Django models to JSON and validate incoming data.\n\n## Views and Viewsets\n\nImplement API views using function-based views, class-based views, and ModelViewSets.',
            'summary': 'Build production-ready REST APIs with Django REST Framework from scratch.',
            'author': 'Admin',
            'published_date': now - timezone.timedelta(days=30),
            'published': True,
            'featured': True,
            'views': 195,
            'get_absolute_url': lambda: '/blog/building-rest-apis-django/',
        })(),
        type('Blog', (), {
            'title': 'Understanding Cyber Threat Landscape in 2024',
            'slug': 'cyber-threat-landscape-2024',
            'content': 'The cybersecurity landscape continues to evolve rapidly. Stay informed about the latest threats and protection strategies.\n\n## Emerging Threats\n\n- Ransomware attacks targeting critical infrastructure\n- AI-powered phishing attacks\n- Supply chain vulnerabilities\n\n## Defense Strategies\n\nImplement a layered security approach with multiple defense mechanisms.\n\n## Incident Response\n\nLearn how to detect, respond to, and recover from security incidents.',
            'summary': 'Stay ahead of cyber threats with this comprehensive guide to the current threat landscape.',
            'author': 'Admin',
            'published_date': now - timezone.timedelta(days=35),
            'published': True,
            'featured': True,
            'views': 210,
            'get_absolute_url': lambda: '/blog/cyber-threat-landscape-2024/',
        })(),
        type('Blog', (), {
            'title': 'Full Stack Development with React and Django',
            'slug': 'full-stack-react-django',
            'content': 'Combine the power of React frontend with Django backend to build modern full-stack applications.\n\n## Project Setup\n\nConfigure your development environment with Django backend and React frontend.\n\n## API Integration\n\nConnect your React app to Django REST API for seamless data flow.\n\n## Authentication\n\nImplement JWT authentication for secure user sessions.',
            'summary': 'Build modern full-stack applications by combining React with Django backend.',
            'author': 'Admin',
            'published_date': now - timezone.timedelta(days=40),
            'published': True,
            'featured': True,
            'views': 165,
            'get_absolute_url': lambda: '/blog/full-stack-react-django/',
        })(),
    ]


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_portfolio_context())
        context['projects'] = Project.objects.filter(featured=True)[:6]
        blogs = Blog.objects.filter(published=True, featured=True)[:3]
        if not blogs.exists():
            blogs = get_default_blogs()[:3]
        context['blogs'] = blogs
        context['contact_form'] = ContactForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            try:
                send_mail(
                    subject=f"Portfolio Contact: {contact.subject}",
                    message=f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(request, 'Message sent successfully! I will get back to you soon.')
            return HttpResponseRedirect(reverse_lazy('home'))
        context = self.get_context_data()
        context['contact_form'] = form
        return self.render_to_response(context)


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    paginate_by = 9
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_portfolio_context())
        context['title'] = 'All Projects'
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'
    query_pk_and_slug = True
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_portfolio_context())
        context['title'] = self.object.title
        context['related_projects'] = Project.objects.exclude(id=self.object.id)[:3]
        return context


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_portfolio_context())
        context['title'] = 'Blog'
        if not context['blogs'].exists():
            context['blogs'] = get_default_blogs()
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'
    query_pk_and_slug = True
    
    def get_queryset(self):
        return Blog.objects.filter(published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_portfolio_context())
        context['title'] = self.object.title
        related = Blog.objects.exclude(id=self.object.id).filter(published=True)[:3]
        if not related.exists():
            related = get_default_blogs()[:3]
        context['related_blogs'] = related
        return context


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_portfolio_context())
        return context
    
    def form_valid(self, form):
        contact = form.save()
        try:
            send_mail(
                subject=f"Portfolio Contact: {contact.subject}",
                message=f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=True,
            )
        except Exception:
            pass
        messages.success(self.request, 'Message sent successfully!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)


class AboutView(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_portfolio_context())
        return context


class ServicesView(TemplateView):
    template_name = 'services.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_portfolio_context())
        return context
