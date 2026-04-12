from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.html import format_html
from django.utils import timezone
from .models import Project, Blog, Contact, SocialLink, Skill, Experience, Education, Profile, Service


def ensure_default_blogs():
    if not Blog.objects.exists():
        now = timezone.now()
        default_blogs = [
            Blog(
                title='Getting Started with Django Web Development',
                slug='getting-started-with-django',
                content='Django is a powerful Python web framework that enables rapid development of secure and maintainable websites. In this comprehensive guide, we will explore the fundamentals of Django and how to build your first web application.\n\n## Why Choose Django?\n\nDjango offers several advantages:\n\n- **Batteries Included**: Comes with built-in admin interface, authentication, and more\n- **Security**: Protects against common vulnerabilities like SQL injection and XSS\n- **Scalability**: Used by Instagram, Pinterest, and other high-traffic sites\n- **Community**: Large ecosystem of packages and excellent documentation\n\n## Setting Up Your First Project\n\n```python\npip install django\ndjango-admin startproject myproject\ncd myproject\npython manage.py runserver\n```\n\nThis creates a basic Django project that you can extend with your own applications.\n\n## Models and Databases\n\nDjango\'s ORM makes it easy to work with databases. Define your models using Python classes and let Django handle the rest.\n\n## Views and URLs\n\nCreate views to handle requests and map them to URLs for routing traffic to the right place.\n\n## Templates\n\nUse Django\'s template language to create dynamic HTML pages that respond to user data.',
                summary='Learn the fundamentals of Django web development and build your first web application with this comprehensive guide.',
                author='Admin',
                published_date=now - timezone.timedelta(days=3),
                published=True,
                featured=True,
                views=150,
            ),
            Blog(
                title='Data Analysis with Python and Pandas',
                slug='data-analysis-python-pandas',
                content='Python has become the go-to language for data analysis, largely thanks to pandas - a powerful library for data manipulation and analysis. This article covers essential techniques for working with data.\n\n## Introduction to Pandas\n\nPandas provides two primary data structures:\n\n- **Series**: One-dimensional labeled array\n- **DataFrame**: Two-dimensional labeled data structure\n\n## Loading and Exploring Data\n\n```python\nimport pandas as pd\ndf = pd.read_csv("data.csv")\nprint(df.head())\nprint(df.describe())\n```\n\n## Data Cleaning Techniques\n\n- Handling missing values\n- Removing duplicates\n- Data type conversion\n- Feature engineering\n\n## Visualization\n\nUse matplotlib and seaborn to create compelling visualizations that tell the story behind your data.\n\n## Statistical Analysis\n\nPerform hypothesis testing, correlation analysis, and regression modeling to extract meaningful insights.',
                summary='Master data analysis with Python and Pandas. Learn essential techniques for loading, cleaning, and analyzing data effectively.',
                author='Admin',
                published_date=now - timezone.timedelta(days=7),
                published=True,
                featured=True,
                views=230,
            ),
            Blog(
                title='Cybersecurity Best Practices for Developers',
                slug='cybersecurity-best-practices',
                content='As developers, we must prioritize security in every application we build. This guide covers essential cybersecurity practices that every developer should know.\n\n## Common Vulnerabilities\n\n1. **SQL Injection**: Never concatenate user input into queries\n2. **XSS (Cross-Site Scripting)**: Always sanitize user input\n3. **CSRF**: Use Django\'s built-in CSRF protection\n4. **Password Storage**: Never store plain-text passwords\n\n## Security Checklist\n\n- [ ] Use HTTPS everywhere\n- [ ] Implement proper authentication\n- [ ] Validate and sanitize all inputs\n- [ ] Keep dependencies updated\n- [ ] Conduct regular security audits\n\n## Secure Coding Practices\n\nWrite code with security in mind from the start. Use parameterized queries, implement proper session management, and follow the principle of least privilege.\n\n## Conclusion\n\nSecurity is not an afterthought - it must be built into every layer of your application from the start.',
                summary='Essential cybersecurity practices every developer should implement to protect their applications from common vulnerabilities.',
                author='Admin',
                published_date=now - timezone.timedelta(days=12),
                published=True,
                featured=True,
                views=180,
            ),
            Blog(
                title='Mastering Microsoft Excel for Business Analytics',
                slug='mastering-microsoft-excel',
                content='Excel remains one of the most powerful tools for business analytics. This guide will take you from basic spreadsheet functions to advanced data analysis techniques.\n\n## Essential Functions\n\nLearn the most important functions like VLOOKUP, INDEX/MATCH, IF statements, and array formulas.\n\n## Pivot Tables\n\nMaster pivot tables to summarize and analyze large datasets quickly. Learn grouping, filtering, and calculated fields.\n\n## Data Visualization\n\nCreate impactful charts and dashboards that communicate insights effectively to stakeholders.\n\n## Macros and VBA\n\nAutomate repetitive tasks and create custom functions with Visual Basic for Applications.\n\n## Power Query\n\nUse Power Query to transform and clean data from multiple sources with ease.',
                summary='Transform your Excel skills from basic to advanced with these essential business analytics techniques.',
                author='Admin',
                published_date=now - timezone.timedelta(days=18),
                published=True,
                featured=True,
                views=320,
            ),
            Blog(
                title='Introduction to Power BI for Data Visualization',
                slug='introduction-to-power-bi',
                content='Power BI is Microsoft\'s powerful business intelligence tool for creating interactive dashboards and reports. Learn how to transform your data into actionable insights.\n\n## Getting Started\n\nConnect to various data sources and import your datasets into Power BI Desktop.\n\n## Data Modeling\n\nCreate relationships between tables and build efficient data models for optimal performance.\n\n## DAX Functions\n\nMaster Data Analysis Expressions to create calculated columns and measures for advanced analytics.\n\n## Visualizations\n\nBuild interactive reports with various chart types, maps, and custom visuals.\n\n## Publishing and Sharing\n\nPublish your reports to Power BI service and share insights with your team.',
                summary='Learn how to create stunning interactive dashboards and reports with Microsoft Power BI.',
                author='Admin',
                published_date=now - timezone.timedelta(days=25),
                published=True,
                featured=True,
                views=275,
            ),
            Blog(
                title='Building REST APIs with Django REST Framework',
                slug='building-rest-apis-django',
                content='Learn how to build robust and scalable REST APIs using Django REST Framework (DRF). This guide covers everything from setup to deployment.\n\n## Setting Up DRF\n\nInstall and configure Django REST Framework in your Django project.\n\n## Serializers\n\nCreate serializers to convert Django models to JSON and validate incoming data.\n\n## Views and Viewsets\n\nImplement API views using function-based views, class-based views, and ModelViewSets.\n\n## Authentication\n\nImplement token-based authentication, JWT, and other security measures.\n\n## Testing and Documentation\n\nWrite tests for your API and generate interactive documentation with Swagger.',
                summary='Build production-ready REST APIs with Django REST Framework from scratch.',
                author='Admin',
                published_date=now - timezone.timedelta(days=30),
                published=True,
                featured=True,
                views=195,
            ),
            Blog(
                title='Understanding Cyber Threat Landscape in 2024',
                slug='cyber-threat-landscape-2024',
                content='The cybersecurity landscape continues to evolve rapidly. Stay informed about the latest threats and protection strategies.\n\n## Emerging Threats\n\n- Ransomware attacks targeting critical infrastructure\n- AI-powered phishing attacks\n- Supply chain vulnerabilities\n- IoT device exploits\n\n## Defense Strategies\n\nImplement a layered security approach with multiple defense mechanisms.\n\n## Incident Response\n\nLearn how to detect, respond to, and recover from security incidents effectively.\n\n## Compliance\n\nUnderstand relevant regulations like GDPR, HIPAA, and PCI-DSS.\n\n## Continuous Learning\n\nStay updated with the latest security research and best practices.',
                summary='Stay ahead of cyber threats with this comprehensive guide to the current threat landscape.',
                author='Admin',
                published_date=now - timezone.timedelta(days=35),
                published=True,
                featured=True,
                views=210,
            ),
            Blog(
                title='Full Stack Development with React and Django',
                slug='full-stack-react-django',
                content='Combine the power of React frontend with Django backend to build modern full-stack applications. This guide shows you how.\n\n## Project Setup\n\nConfigure your development environment with Django backend and React frontend.\n\n## API Integration\n\nConnect your React app to Django REST API for seamless data flow.\n\n## Authentication\n\nImplement JWT authentication for secure user sessions.\n\n## State Management\n\nUse React Context and Redux for efficient state management.\n\n## Deployment\n\nDeploy your full-stack application to production with Docker and cloud platforms.',
                summary='Build modern full-stack applications by combining React with Django backend.',
                author='Admin',
                published_date=now - timezone.timedelta(days=40),
                published=True,
                featured=True,
                views=165,
            ),
        ]
        Blog.objects.bulk_create(default_blogs)


def ensure_default_services():
    if not Service.objects.exists():
        default_services = [
            Service(
                title='Full Stack Development',
                description='End-to-end web application development with modern technologies.',
                icon_class='fas fa-code',
                icon_color='sky',
                features=['Django & Flask', 'React & Next.js', 'RESTful APIs', 'Responsive Design'],
                is_active=True,
            ),
            Service(
                title='Data Analysis',
                description='Transform raw data into actionable insights for better decision-making.',
                icon_class='fas fa-chart-line',
                icon_color='purple',
                features=['Python & Pandas', 'SQL & Excel', 'Data Visualization', 'Statistical Analysis'],
                is_active=True,
            ),
            Service(
                title='Microsoft Suite',
                description='Professional spreadsheet, presentation, and document solutions.',
                icon_class='fas fa-file-excel',
                icon_color='blue',
                features=['Excel & Power BI', 'Word & PowerPoint', 'VBA Automation', 'Data Dashboards'],
                is_active=True,
            ),
            Service(
                title='Cybersecurity Analysis',
                description='Protect your digital assets with comprehensive security assessments.',
                icon_class='fas fa-shield-alt',
                icon_color='red',
                features=['Vulnerability Assessment', 'Security Audits', 'Risk Analysis', 'Security Best Practices'],
                is_active=True,
            ),
            Service(
                title='Database Design',
                description='Efficient database architecture and optimization for scalable applications.',
                icon_class='fas fa-database',
                icon_color='emerald',
                features=['PostgreSQL & MySQL', 'MongoDB', 'Redis Caching', 'Data Migration'],
                is_active=True,
            ),
            Service(
                title='Cloud & DevOps',
                description='Deployment, CI/CD, and cloud infrastructure management.',
                icon_class='fas fa-cloud',
                icon_color='orange',
                features=['AWS & GCP', 'Docker & Kubernetes', 'CI/CD Pipelines', 'Monitoring'],
                is_active=True,
            ),
        ]
        Service.objects.bulk_create(default_services)


def ensure_default_skills():
    if not Skill.objects.exists():
        default_skills = [
            Skill(name='Python', category='backend', icon_class='fab fa-python', proficiency=90, is_active=True),
            Skill(name='Django', category='backend', icon_class='fas fa-server', proficiency=85, is_active=True),
            Skill(name='JavaScript', category='frontend', icon_class='fab fa-js', proficiency=85, is_active=True),
            Skill(name='React', category='frontend', icon_class='fab fa-react', proficiency=80, is_active=True),
            Skill(name='PostgreSQL', category='database', icon_class='fas fa-database', proficiency=85, is_active=True),
            Skill(name='Data Analysis', category='other', icon_class='fas fa-chart-line', proficiency=85, is_active=True),
            Skill(name='Excel', category='other', icon_class='fas fa-file-excel', proficiency=95, is_active=True),
            Skill(name='Power BI', category='other', icon_class='fas fa-chart-pie', proficiency=85, is_active=True),
            Skill(name='Cybersecurity', category='other', icon_class='fas fa-shield-alt', proficiency=75, is_active=True),
            Skill(name='Docker', category='devops', icon_class='fab fa-docker', proficiency=80, is_active=True),
        ]
        Skill.objects.bulk_create(default_skills)


class CustomAdminSite(AdminSite):
    site_header = "Portfolio Admin"
    site_title = "Portfolio Admin"
    index_title = "Welcome to Portfolio Administration"
    login_template = 'admin/login.html'
    index_template = 'admin/base.html'
    
    def each_context(self, request):
        ensure_default_blogs()
        ensure_default_services()
        ensure_default_skills()
        context = super().each_context(request)
        context.update({
            'gradient_text_class': 'gradient-text',
            'total_projects': Project.objects.count(),
            'total_blogs': Blog.objects.filter(published=True).count(),
            'total_services': Service.objects.count(),
            'total_skills': Skill.objects.count(),
            'total_messages': Contact.objects.count(),
            'unread_messages': Contact.objects.filter(read=False).count(),
            'recent_projects': Project.objects.all()[:5],
            'recent_messages': Contact.objects.all()[:5],
            'recent_blogs': Blog.objects.all()[:5],
            'profile': Profile.objects.first(),
        })
        return context


admin_site = CustomAdminSite(name='admin')


@admin.register(Project, site=admin_site)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_technologies', 'created_date', 'featured', 'image_preview', 'order']
    list_filter = ['featured', 'created_date']
    search_fields = ['title', 'description', 'technologies']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['featured', 'order']
    date_hierarchy = 'created_date'
    readonly_fields = ['created_date']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'technologies')
        }),
        ('Media & Links', {
            'fields': ('image', 'external_link', 'github_link')
        }),
        ('Settings', {
            'fields': ('featured', 'order', 'created_date'),
            'classes': ('collapse',)
        }),
    )
    
    def display_technologies(self, obj):
        if not obj.technologies:
            return '-'
        techs = [t.strip() for t in obj.technologies.split(',')]
        html = ''
        for tech in techs[:5]:
            html += format_html('<span class="px-2 py-1 bg-slate-700 text-slate-300 text-xs rounded">{}</span> ', tech)
        if len(techs) > 5:
            html += format_html('<span class="px-2 py-1 bg-slate-600 text-slate-400 text-xs rounded">+{}</span>', len(techs)-5)
        return html
    display_technologies.short_description = 'Technologies'
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 80px; height: 50px; object-fit: cover; border-radius: 8px;" />', obj.image.url)
        return format_html('<span class="text-slate-500"><i class="fas fa-image"></i></span>')
    image_preview.short_description = 'Preview'


@admin.register(Blog, site=admin_site)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'published', 'featured', 'display_views', 'word_count']
    list_filter = ['published', 'featured', 'published_date', 'author']
    search_fields = ['title', 'content', 'summary']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['published', 'featured']
    date_hierarchy = 'published_date'
    readonly_fields = ['created_date', 'updated_date', 'word_count', 'views']
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'content')
        }),
        ('Metadata', {
            'fields': ('summary', 'image', 'author', 'published', 'featured')
        }),
        ('Statistics', {
            'fields': ('views', 'published_date'),
            'classes': ('collapse',)
        }),
        ('Dates', {
            'fields': ('created_date', 'updated_date'),
            'classes': ('collapse',)
        }),
    )
    
    def display_views(self, obj):
        return format_html('<span class="px-2 py-1 bg-slate-700 text-slate-300 text-xs rounded"><i class="fas fa-eye mr-1"></i>{}</span>', obj.views)
    display_views.short_description = 'Views'
    
    def word_count(self, obj):
        return f"{len(str(obj.content).split())} words"
    word_count.short_description = 'Words'


@admin.register(Contact, site=admin_site)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_date', 'read']
    list_filter = ['read', 'created_date']
    search_fields = ['name', 'email', 'subject', 'message']
    list_editable = ['read']
    date_hierarchy = 'created_date'
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_date']
    ordering = ['-created_date']
    
    def has_add_permission(self, request):
        return False
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        contact = self.get_object(request, object_id)
        if contact and not contact.read:
            contact.read = True
            contact.save()
        return super().change_view(request, object_id, form_url, extra_context)


@admin.register(Profile, site=admin_site)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email']
    list_filter = []
    search_fields = []
    readonly_fields = ['updated_date']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'subtitle', 'profile_image')
        }),
        ('Contact Details', {
            'fields': ('email', 'phone', 'location', 'website')
        }),
        ('About Section', {
            'fields': ('about_title', 'about_subtitle', 'about_content', 'about_image')
        }),
        ('Hero Stats', {
            'fields': ('hero_stats',),
            'description': 'Enter as JSON: {"projects": "50+", "years": "3+", "clients": "30+"}',
            'classes': ('collapse',)
        }),
        ('Files', {
            'fields': ('resume_cv',),
        }),
        ('Footer', {
            'fields': ('response_time', 'footer_text', 'footer_copyright'),
            'classes': ('collapse',)
        }),
        ('SEO', {
            'fields': ('seo_title', 'seo_description', 'seo_keywords', 'google_analytics_id'),
            'classes': ('collapse',)
        }),
        ('Last Updated', {
            'fields': ('updated_date',),
            'classes': ('collapse',)
        }),
    )
    
    def display_socials(self, obj):
        count = SocialLink.objects.filter(is_active=True).count()
        return format_html('<span class="px-2 py-1 bg-slate-700 text-slate-300 text-xs rounded"><i class="fas fa-share-alt mr-1"></i>{} links</span>', count)
    display_socials.short_description = 'Social Links'
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Service, site=admin_site)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_preview', 'display_features', 'order', 'is_active']
    list_filter = ['is_active']
    list_editable = ['order', 'is_active']
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'description', 'icon_class', 'icon_color')
        }),
        ('Features', {
            'fields': ('features',),
            'description': 'Enter as JSON array: ["Feature 1", "Feature 2", "Feature 3"]',
        }),
        ('Settings', {
            'fields': ('order', 'is_active'),
        }),
    )
    
    def icon_preview(self, obj):
        color_class = f"text-{obj.icon_color}-400"
        return format_html('<i class="{} text-xl {}"></i>', obj.icon_class, color_class)
    icon_preview.short_description = 'Icon'
    
    def display_features(self, obj):
        if obj.features:
            return f"{len(obj.features)} features"
        return "No features"
    display_features.short_description = 'Features'


@admin.register(SocialLink, site=admin_site)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_platform', 'url', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['name', 'platform']
    
    def display_platform(self, obj):
        icons = {
            'github': 'fab fa-github',
            'linkedin': 'fab fa-linkedin',
            'twitter': 'fab fa-twitter',
            'facebook': 'fab fa-facebook',
            'instagram': 'fab fa-instagram',
            'youtube': 'fab fa-youtube',
            'discord': 'fab fa-discord',
            'stackoverflow': 'fab fa-stack-overflow',
            'dribbble': 'fab fa-dribbble',
            'behance': 'fab fa-behance',
            'medium': 'fab fa-medium',
            'dev': 'fab fa-dev',
            'telegram': 'fab fa-telegram',
            'whatsapp': 'fab fa-whatsapp',
        }
        icon = icons.get(obj.platform, 'fas fa-link')
        return format_html('<i class="{} text-xl"></i>', icon)
    display_platform.short_description = 'Icon'


@admin.register(Skill, site=admin_site)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'display_proficiency', 'order', 'is_active']
    list_filter = ['category', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['name']
    
    def display_proficiency(self, obj):
        color = 'emerald' if obj.proficiency >= 80 else 'sky' if obj.proficiency >= 60 else 'yellow' if obj.proficiency >= 40 else 'red'
        return format_html('''
            <div class="flex items-center gap-2">
                <div class="w-24 h-2 bg-slate-700 rounded-full overflow-hidden">
                    <div class="h-full bg-{}-500" style="width: {}%"></div>
                </div>
                <span class="text-sm text-slate-400">{}%</span>
            </div>
        ''', color, obj.proficiency, obj.proficiency)
    display_proficiency.short_description = 'Proficiency'


@admin.register(Experience, site=admin_site)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'display_dates', 'is_current', 'order', 'is_active']
    list_filter = ['is_current', 'is_active']
    list_editable = ['order', 'is_active', 'is_current']
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'company', 'location')
        }),
        ('Details', {
            'fields': ('description', 'start_date', 'end_date', 'is_current')
        }),
        ('Settings', {
            'fields': ('order', 'is_active'),
            'classes': ('collapse',)
        }),
    )
    
    def display_dates(self, obj):
        if obj.is_current:
            return format_html('<span class="text-slate-400">{} - Present</span>', obj.start_date.strftime("%b %Y"))
        elif obj.end_date:
            return format_html('<span class="text-slate-400">{} - {}</span>', obj.start_date.strftime("%b %Y"), obj.end_date.strftime("%b %Y"))
        return obj.start_date.strftime("%b %Y")
    display_dates.short_description = 'Duration'


@admin.register(Education, site=admin_site)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'display_dates', 'is_current', 'order', 'is_active']
    list_filter = ['is_current', 'is_active']
    list_editable = ['order', 'is_active', 'is_current']
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('degree', 'institution', 'location')
        }),
        ('Details', {
            'fields': ('description', 'start_date', 'end_date', 'is_current')
        }),
        ('Settings', {
            'fields': ('order', 'is_active'),
            'classes': ('collapse',)
        }),
    )
    
    def display_dates(self, obj):
        if obj.is_current:
            return format_html('<span class="text-slate-400">{} - Present</span>', obj.start_date.strftime("%Y"))
        elif obj.end_date:
            return format_html('<span class="text-slate-400">{} - {}</span>', obj.start_date.strftime("%Y"), obj.end_date.strftime("%Y"))
        return obj.start_date.strftime("%Y")
    display_dates.short_description = 'Duration'
