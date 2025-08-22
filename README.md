# FastHTML Static Site Generator

A minimal personal website built with [FastHTML](https://fastht.ml) that generates pure static HTML files for GitHub Pages hosting.

## Features

- ✨ **Static HTML Generation**: No server runtime required
- 📱 **Responsive Design**: Works perfectly on all devices
- ♿ **Accessible**: Semantic HTML with proper ARIA labels
- 🔍 **SEO Optimized**: Open Graph and Twitter Card meta tags
- 🎨 **Clean Styling**: Modern, minimal CSS design
- 🚀 **GitHub Pages Ready**: Includes `.nojekyll` file

## Pages

- **Home** (`index.html`) - Welcome page with project overview
- **About** (`about.html`) - Personal information and technologies

## Quick Start

### Prerequisites

- Python 3.11+
- FastHTML (`python-fasthtml>=0.6.9`)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/xstraven/blog-fasthtml.git
cd blog-fasthtml
```

2. Install FastHTML:
```bash
pip install python-fasthtml
```

### Generate the Site

Run the static site generator:

```bash
python generate_site.py
```

This will create:
- `docs/index.html` - Home page
- `docs/about.html` - About page  
- `docs/.nojekyll` - Prevents Jekyll processing

### Local Preview

You can preview the generated site locally by serving the `docs/` directory:

```bash
# Using Python's built-in server
cd docs
python -m http.server 8000

# Then visit http://localhost:8000
```

## GitHub Pages Setup

To deploy this site on GitHub Pages:

1. **Push your changes** to GitHub
2. **Go to repository Settings** → Pages
3. **Set Source** to "Deploy from a branch"
4. **Select Branch** as `main` (or your default branch)
5. **Select Folder** as `/docs`
6. **Save** and wait for deployment

Your site will be available at: `https://yourusername.github.io/repository-name/`

### Custom Domain (Optional)

To use a custom domain:

1. Add a `CNAME` file to the `docs/` directory with your domain
2. Configure DNS settings with your domain provider
3. Enable "Enforce HTTPS" in GitHub Pages settings

## Customization

### Modify Content

Edit the functions in `generate_site.py`:

- `create_home_page()` - Customize home page content
- `create_about_page()` - Customize about page content
- `create_base_layout()` - Modify site-wide styling and structure

### Add New Pages

1. Create a new function for your page content
2. Add it to the `generate_static_site()` function
3. Update navigation in `create_base_layout()`

### Styling

The CSS is embedded in the `create_base_layout()` function. Key features:

- **Mobile-first responsive design**
- **Accessible focus indicators**
- **Modern card-based layout**
- **Clean typography**

## Project Structure

```
blog-fasthtml/
├── generate_site.py      # Static site generator
├── docs/                 # Generated static files (GitHub Pages source)
│   ├── index.html
│   ├── about.html
│   └── .nojekyll
├── pyproject.toml        # Project configuration
└── README.md            # This file
```

## Technologies Used

- **[FastHTML](https://fastht.ml)** - Python web framework for generating HTML
- **Python 3.12** - Programming language
- **GitHub Pages** - Static site hosting
- **Semantic HTML5** - Accessible markup
- **CSS3** - Modern styling with Flexbox and Grid

## Why FastHTML?

FastHTML makes it incredibly easy to generate clean, semantic HTML using Python. Benefits:

- 🐍 **Pure Python** - No need to learn templating languages
- 🔧 **Functional Components** - Reusable, composable HTML elements  
- 📏 **Minimal Dependencies** - Just FastHTML, no complex build tools
- 🎯 **Type Safety** - Leverage Python's type system for HTML generation

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

---

Built with ❤️ using [FastHTML](https://fastht.ml)