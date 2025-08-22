#!/usr/bin/env python3
"""
Static site generator using FastHTML.
Generates static HTML files for GitHub Pages.
"""

import os
from pathlib import Path
from fasthtml.common import *

# Output directory for static files
DOCS_DIR = Path("docs")

def create_base_layout(title: str, content, description: str = "Personal website"):
    """Create the base HTML layout with navigation, content, and footer."""
    
    # Meta tags for SEO and social media
    meta_tags = [
        Meta(charset="utf-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1"),
        Meta(name="description", content=description),
        # Open Graph tags
        Meta(property="og:title", content=title),
        Meta(property="og:description", content=description),
        Meta(property="og:type", content="website"),
        Meta(property="og:url", content="https://xstraven.github.io/blog-fasthtml/"),
        # Twitter Card tags
        Meta(name="twitter:card", content="summary"),
        Meta(name="twitter:title", content=title),
        Meta(name="twitter:description", content=description),
    ]
    
    # Basic responsive CSS
    styles = Style("""
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f8f9fa;
        }
        
        header {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        nav ul {
            list-style: none;
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
        }
        
        nav a {
            color: #007bff;
            text-decoration: none;
            font-weight: 500;
            padding: 8px 12px;
            border-radius: 4px;
            transition: background-color 0.2s;
        }
        
        nav a:hover, nav a:focus {
            background-color: #e7f3ff;
            outline: 2px solid #007bff;
        }
        
        nav a[aria-current="page"] {
            background-color: #007bff;
            color: white;
        }
        
        main {
            background: #fff;
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        h1 {
            color: #2c3e50;
            margin-bottom: 20px;
            font-size: 2.5rem;
        }
        
        h2 {
            color: #34495e;
            margin: 30px 0 15px 0;
            font-size: 1.8rem;
        }
        
        p {
            margin-bottom: 15px;
            font-size: 1.1rem;
        }
        
        footer {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            color: #666;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .highlight {
            background-color: #fff3cd;
            padding: 15px;
            border-radius: 4px;
            border-left: 4px solid #ffc107;
            margin: 20px 0;
        }
        
        @media (max-width: 600px) {
            body {
                padding: 10px;
            }
            
            header, main, footer {
                padding: 15px;
            }
            
            h1 {
                font-size: 2rem;
            }
            
            nav ul {
                flex-direction: column;
                gap: 10px;
            }
        }
    """)
    
    return Html(
        Head(
            *meta_tags,
            Title(title),
            styles
        ),
        Body(
            Header(
                Nav(
                    Ul(
                        Li(A("Home", href="index.html", **{"aria-current": "page" if "Home" in title else None})),
                        Li(A("About", href="about.html", **{"aria-current": "page" if "About" in title else None}))
                    ),
                    role="navigation",
                    **{"aria-label": "Main navigation"}
                )
            ),
            Main(
                content,
                role="main"
            ),
            Footer(
                P("Built with FastHTML • © 2024"),
                role="contentinfo"
            )
        ),
        lang="en"
    )

def create_home_page():
    """Create the home page content."""
    content = Div(
        H1("Welcome to My Personal Website"),
        P("Hello! This is a minimal personal website built with FastHTML and hosted on GitHub Pages."),
        Div(
            P("🚀 This site demonstrates:"),
            Ul(
                Li("Static HTML generation with FastHTML"),
                Li("Responsive design that works on all devices"),
                Li("Accessible semantic markup"),
                Li("Clean, modern styling"),
                Li("SEO and social media optimization")
            ),
            className="highlight"
        ),
        P("FastHTML makes it easy to generate clean, semantic HTML using Python. This entire site is built with just a few lines of Python code!"),
        H2("About This Project"),
        P("This website showcases how to create a static site generator using FastHTML that outputs pure HTML files suitable for GitHub Pages hosting. No server runtime required!"),
        P("Check out the ", A("About page", href="about.html"), " to learn more about me, or view the source code on GitHub.")
    )
    
    return create_base_layout(
        title="Home - Personal Website",
        content=content,
        description="Personal website built with FastHTML - static site generator demo"
    )

def create_about_page():
    """Create the about page content."""
    content = Div(
        H1("About Me"),
        P("Hi there! I'm a developer passionate about building simple, effective web solutions."),
        H2("What I Do"),
        P("I enjoy exploring modern web technologies and creating tools that make development easier. This site is a perfect example - using FastHTML to generate static sites with minimal complexity."),
        H2("Technologies I Love"),
        Ul(
            Li("Python for backend development and automation"),
            Li("FastHTML for rapid web development"),
            Li("Static site generators for fast, secure websites"),
            Li("GitHub Pages for simple, free hosting")
        ),
        H2("Get In Touch"),
        P("Feel free to reach out if you'd like to collaborate on a project or just chat about technology!"),
        Div(
            P("💡 This entire website is generated from Python code using FastHTML!"),
            className="highlight"
        )
    )
    
    return create_base_layout(
        title="About - Personal Website", 
        content=content,
        description="Learn more about me and my work with web technologies"
    )

def generate_static_site():
    """Generate all static HTML files."""
    # Create docs directory if it doesn't exist
    DOCS_DIR.mkdir(exist_ok=True)
    
    # Generate home page
    home_html = create_home_page()
    with open(DOCS_DIR / "index.html", "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n")
        f.write(to_xml(home_html))
    
    # Generate about page
    about_html = create_about_page()
    with open(DOCS_DIR / "about.html", "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n")
        f.write(to_xml(about_html))
    
    # Create .nojekyll file to prevent Jekyll processing
    with open(DOCS_DIR / ".nojekyll", "w") as f:
        f.write("")
    
    print("✅ Static site generated successfully!")
    print(f"📁 Files created in {DOCS_DIR}:")
    for file in DOCS_DIR.iterdir():
        print(f"   - {file.name}")

if __name__ == "__main__":
    generate_static_site()