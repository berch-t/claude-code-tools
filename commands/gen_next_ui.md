**GEN NEXT UI - SOTA LANDING PAGE GENERATOR**

Create professional Next.js landing page templates by extracting UI component wisdom from videos/content and generating multiple SOTA templates with parallel agent coordination.

**Variables:**
theme: $ARGUMENTS
iterations: $ARGUMENTS (default: 1)
source_url: $ARGUMENTS (optional)
output_dir: $ARGUMENTS (default: ./next_ui_templates)
library: $ARGUMENTS (optional)

**ARGUMENTS PARSING:**
Parse the following arguments from "$ARGUMENTS":
1. `theme` - Theme specification (required): sota_ai_engineer_portfolio, saas_dashboard, fintech_landing, ecommerce_luxury, agency_creative, etc.
2. `iterations` - Number of template variations to generate (1-10, default: 1)
3. `source_url` - Optional URL for component library extraction (YouTube, component websites, documentation sites)
4. `output_dir` - Directory where templates will be saved (default: ./next_ui_templates)
5. `library` - Force specific component library (shadcn, reactbits, aceternity, etc.)

**PHASE 1: WISDOM & COMPONENT EXTRACTION**
If source URL is provided, detect and process accordingly:

**URL Detection & Processing:**
- **YouTube URLs** (youtube.com, youtu.be): Extract video transcription using Daniel Miessler's extractwisdom pattern
- **Component Library Sites** (ui.aceternity.com, reactbits.dev, ui.shadcn.com): Web scrape component documentation and examples
- **Documentation Sites** (nextjs.org, tailwindcss.com): Extract best practices and implementation patterns
- **Design System Sites** (design.systems, material.io): Extract design principles and component specifications
- **GitHub Repositories** (github.com): Analyze component code and usage examples

**Extraction Strategy by URL Type:**
1. **YouTube Processing**: Use existing wisdom extraction pipeline for video content
2. **Website Processing**: Use WebFetch tool to extract component documentation, code examples, and design patterns
3. **Focus Areas**: UI component libraries, design patterns, implementation details, styling approaches, best practices
4. **Output**: Save extracted wisdom to `{theme}_component_wisdom_{timestamp}.md`

**PHASE 2: THEME ANALYSIS & TEMPLATE STRATEGY**
Analyze the requested theme and determine:

**Available Themes:**
- `sota_ai_engineer_portfolio`: Cutting-edge developer portfolio with interactive demos
- `saas_dashboard`: Modern SaaS landing with feature highlights and pricing
- `fintech_landing`: Financial tech platform with trust indicators and security
- `ecommerce_luxury`: High-end e-commerce with elegant product showcases
- `agency_creative`: Creative agency with bold visuals and case studies
- `startup_tech`: Tech startup with growth metrics and investor appeal
- `healthcare_platform`: Medical/health platform with compliance and trust
- `education_online`: Online learning platform with course previews
- `real_estate_modern`: Property platform with interactive maps and listings
- `restaurant_premium`: Premium dining with menu and reservation system

**Theme Requirements:**
- Component selection strategy for the theme
- Color schemes and typography requirements
- Layout patterns and user flow considerations
- Business-specific features and sections needed
- Mobile responsiveness and accessibility standards

**PHASE 3: PARALLEL TEMPLATE GENERATION**
Deploy Sub Agents to generate template variations in parallel:

**Agent Distribution Strategy:**
- For iterations 1-3: Launch all agents simultaneously
- For iterations 4-10: Launch in batches of 3 agents for coordination
- Each agent generates one complete, unique template variation

**Agent Assignment Protocol:**
Each Sub Agent receives:
1. **Theme Context**: Complete theme analysis and requirements
2. **Component Wisdom**: Extracted component patterns (if from YouTube)
3. **Iteration Assignment**: Specific variation number and creative direction
4. **Library Specification**: Component library to use (shadcn/ui default)
5. **Template Structure**: Required Next.js project structure

**Agent Task Specification:**
```
TASK: Generate Next.js template iteration [NUMBER] for theme [THEME]

You are Sub Agent [X] generating template variation [NUMBER] for [THEME].

CONTEXT:
- Theme: [THEME] with specific business requirements
- Component Wisdom: [Extracted patterns from video if provided]
- Your iteration number: [NUMBER]
- Creative direction: [Specific approach - e.g., "conversion-focused", "visual-heavy", "interactive-demo"]
- Component library: [LIBRARY]

REQUIREMENTS:
1. Create complete Next.js 14+ project with App Router
2. Use TypeScript and Tailwind CSS
3. Implement responsive design (mobile-first)
4. Include [THEME]-specific sections and features
5. Use modern component patterns from wisdom extraction
6. Follow Next.js best practices and performance optimization
7. Create production-ready, deployable template

PROJECT STRUCTURE:
- /app (App Router structure)
- /components (Reusable UI components)
- /lib (Utilities and configurations)
- /public (Assets and images)
- package.json with proper dependencies
- tailwind.config.js optimized for theme
- README.md with deployment instructions

TEMPLATE SECTIONS (based on theme):
[Dynamic section list based on selected theme]

DELIVERABLE: Complete Next.js project in folder [THEME]_template_[NUMBER]
```

**PHASE 4: TEMPLATE SPECIFICATIONS BY THEME**

**SOTA AI Engineer Portfolio:**
- Hero with animated code snippets and typing effect
- Interactive project showcase with live demos
- Skills visualization with animated charts
- GitHub contribution graph integration
- Tech stack icons with hover effects
- Contact form with validation
- Dark/light mode toggle
- Blog/articles section with MDX support

**SaaS Dashboard:**
- Hero with product screenshots and demo video
- Feature grid with icons and descriptions
- Pricing tiers with feature comparison
- Customer testimonials carousel
- Integration logos and partnerships
- FAQ accordion section
- CTA sections strategically placed
- Footer with all necessary links

**Fintech Landing:**
- Trust indicators and security badges
- Financial data visualizations
- Compliance and regulatory information
- Customer success stories
- Mobile app preview and download links
- Security-first design approach
- Clear value proposition
- Demo request form

**PHASE 5: COMPONENT LIBRARY INTEGRATION**

**Supported Libraries:**
- **shadcn/ui** (default): Modern, accessible, customizable
- **reactbits**: Premium components with animations
- **aceternity**: Cutting-edge UI with advanced effects
- **nextui**: Fast, modern React UI library
- **mantine**: Full-featured components and hooks
- **custom**: Hand-crafted components based on extracted wisdom

**Integration Strategy:**
- Install appropriate component library dependencies
- Configure theme system and design tokens
- Implement components following library patterns
- Customize styling to match theme requirements
- Ensure accessibility and performance standards

**PHASE 6: QUALITY ASSURANCE & OPTIMIZATION**

**Template Requirements:**
- Next.js 14+ with App Router
- TypeScript strict mode enabled
- Tailwind CSS with custom configuration
- Responsive design (mobile, tablet, desktop)
- SEO optimization with metadata
- Performance optimization (images, fonts, bundle)
- Accessibility compliance (WCAG guidelines)
- Clean, production-ready code

**File Organization:**
- Consistent naming conventions
- Proper component hierarchy
- Reusable utility functions
- Optimized asset loading
- Environment configuration
- Deployment configuration (Vercel, Netlify ready)

**PHASE 7: DOCUMENTATION & DEPLOYMENT**

Each template includes:
- **README.md**: Setup, customization, deployment instructions
- **CUSTOMIZATION.md**: Theme modification guide
- **DEPLOYMENT.md**: Platform-specific deployment guides
- **COMPONENTS.md**: Component usage documentation
- **package.json**: All necessary dependencies and scripts

**Deployment Ready:**
- Vercel deployment configuration
- Netlify deployment configuration
- Docker configuration for self-hosting
- Environment variables template
- Build optimization settings

**EXECUTION PRINCIPLES:**

**Theme Consistency:**
- Each iteration maintains theme coherence while exploring different approaches
- Visual hierarchy and branding consistency
- User experience optimized for theme's target audience
- Business-specific features properly implemented

**Technical Excellence:**
- Modern Next.js patterns and best practices
- Clean, maintainable, well-documented code
- Performance optimized (Core Web Vitals)
- SEO and accessibility compliant
- Mobile-first responsive design

**Creative Diversity:**
- Different layout approaches per iteration
- Varied component usage and styling
- Unique interactive elements and animations
- Different content organization strategies
- Distinct visual treatments within theme constraints

**Production Ready:**
- Easy to customize and extend
- Clear documentation and setup instructions
- Deployment ready with minimal configuration
- Professional code quality and organization
- Scalable architecture for future enhancements

**COMMAND EXAMPLES:**

```bash
# Single template for AI portfolio
/gen_next_ui --theme sota_ai_engineer_portfolio

# Multiple SaaS variations
/gen_next_ui --theme saas_dashboard --iterations 3

# Extract from component library website
/gen_next_ui https://ui.aceternity.com --theme fintech_landing --iterations 2

# Extract from reactbits.dev
/gen_next_ui https://reactbits.dev --theme agency_creative --iterations 3

# Extract from Shadcn documentation  
/gen_next_ui https://ui.shadcn.com/docs/components --theme ecommerce_luxury

# YouTube video extraction (original functionality)
/gen_next_ui https://youtube.com/watch?v=reactbits-demo --theme startup_tech --iterations 2

# GitHub repository analysis
/gen_next_ui https://github.com/shadcn-ui/ui --theme healthcare_platform

# Specific library with custom output
/gen_next_ui --theme agency_creative --library aceternity --output_dir ./my_templates --iterations 5

# Combined: Extract from site + force different library
/gen_next_ui https://ui.aceternity.com --theme saas_dashboard --library shadcn --iterations 4
```

**OUTPUT STRUCTURE:**
```
next_ui_templates/
├── [theme]_template_1/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── public/
│   ├── package.json
│   ├── tailwind.config.js
│   └── README.md
├── [theme]_template_2/
│   └── [same structure]
└── generation_summary.md
```

**ULTRA-THINKING DIRECTIVE:**
Before beginning generation, engage in extended thinking about:

**URL Processing & Wisdom Extraction:**
- Detect URL type and choose appropriate extraction strategy
- For component libraries: Focus on component APIs, styling patterns, and implementation examples  
- For documentation: Extract architectural patterns and best practices
- How to translate extracted wisdom into actionable template requirements

**Theme Analysis & Requirements:**
- Deep analysis of the selected theme's business requirements
- Component selection strategy aligned with theme needs
- Visual hierarchy and user experience considerations
- Technical requirements and integration patterns

**Template Generation Strategy:**
- How to create production-ready, customizable templates
- Balancing modern aesthetics with functional requirements
- Ensuring responsive design and accessibility compliance
- Code organization and documentation standards

**EXECUTION WORKFLOW:**

**STEP 1: ARGUMENT PARSING & VALIDATION**
Parse the provided arguments and validate:
- Extract theme specification (required)
- Extract iterations count (default to 1 if not specified)
- Extract source_url if provided
- Extract output_dir (default to ./next_ui_templates)
- Extract library preference if specified

**STEP 2: WISDOM EXTRACTION (if URL provided)**
If source_url is detected:
1. Identify URL type (YouTube, component library, documentation, GitHub)
2. Execute appropriate extraction strategy:
   - YouTube: Use wisdom extraction pipeline
   - Websites: Use WebFetch tool with component-focused prompts
   - GitHub: Analyze repository structure and component patterns
3. Save extracted wisdom to `{theme}_component_wisdom_{timestamp}.md`
4. Summarize key patterns for template generation

**STEP 3: THEME REQUIREMENTS ANALYSIS**
Analyze the specified theme and determine:
- Required sections and components
- Visual design requirements
- Business-specific functionality
- Target audience and use cases
- Technical implementation patterns

**STEP 4: TEMPLATE GENERATION COORDINATION**
For single iteration (iterations=1):
- Generate one comprehensive template directly
For multiple iterations (iterations>1):
- Deploy parallel Sub Agents using Task tool
- Assign unique creative directions to each agent
- Coordinate to prevent duplication

**STEP 5: TEMPLATE IMPLEMENTATION**
Create complete Next.js project with:
- Modern project structure (App Router)
- Component library integration
- Responsive design implementation
- Documentation and deployment configuration

**STEP 6: QUALITY VALIDATION & DOCUMENTATION**
- Validate template completeness and functionality
- Generate comprehensive documentation
- Create deployment guides
- Summarize generation results

Begin execution with deep analysis of the provided arguments and proceed systematically through each step, leveraging extracted wisdom and parallel coordination for maximum efficiency and quality.