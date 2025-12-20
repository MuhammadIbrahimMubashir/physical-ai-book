// @ts-check
const config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'Learn Robotics and Physical AI step by step',
  url: 'https://muhammadibrahimmubashir.github.io',
  baseUrl: '/physical-ai-book/',

  onBrokenLinks: 'warn',          
  onBrokenMarkdownLinks: 'warn',  

  favicon: 'img/favicon.ico',
  organizationName: 'MuhammadIbrahimMubashir', 
  projectName: 'physical-ai-book', 

  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          path: 'docs',
          routeBasePath: '/', 
          sidebarPath: require.resolve('./sidebars.js')
        },
      }
    ]
  ]
};

module.exports = config;
