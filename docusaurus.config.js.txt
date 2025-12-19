// @ts-check
const config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'Learn Robotics and Physical AI step by step',
  url: 'https://MuhammadIbrahimMubashir.github.io',
  baseUrl: '/Physical-Ai-Book/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'MuhammadIbrahimMubashir', 
  projectName: 'Physical-Ai-Book',
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          path: 'docs',
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js')
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css')
        }
      }
    ]
  ]
};

module.exports = config;
