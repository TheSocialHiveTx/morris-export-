import sys

file_path = r'c:\Users\suppo\OneDrive\Desktop\Developer\morris-export-\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update navLinks array
start_nav_links = text.find('const navLinks = [')
end_nav_links = text.find('];', start_nav_links) + 2

new_nav_links = '''const navLinks = [
      { name: 'Services', path: '#/services' },
      { name: 'Success Stories', path: '#/success-stories' },
      { name: 'About & History', path: '#/about-us' },
      { name: 'Customer Hub', path: '#/customer-center' }
    ];'''

text = text[:start_nav_links] + new_nav_links + text[end_nav_links:]

# 2. Add renderSuccessStories() after renderHome()
# Let's insert it before `function renderAbout()`
start_about = text.find('function renderAbout() {')
success_stories_code = '''function renderSuccessStories() {
      const stories = [
        {
          client: "Global Petrochemical",
          title: "Delta Refinery Expansion",
          metric: "40+ Oversized Units",
          img: "images/containerization/container1.webp",
          desc: "Managed the transloading, securing, and export packing of massive refinery components destined for South America. Zero incidents, delivered ahead of schedule."
        },
        {
          client: "Aerospace Defense",
          title: "Fragile Instrumentation Transport",
          metric: "Shock-proof Crating",
          img: "images/mpacttech/mpact2.webp",
          desc: "Engineered specialized vapor-barrier and shock-absorbing crates for highly sensitive satellite instrumentation."
        },
        {
          client: "Heavy Manufacturing",
          title: "Factory Relocation",
          metric: "Turnkey Operation",
          img: "images/facilityrelocation/facilityrelocation].webp",
          desc: "Dismantled, packed, and transported an entire manufacturing line from Texas to Mexico. Coordinated heavy haul, crating, and border logistics."
        }
      ];

      const storiesHtml = stories.map((story, idx) => `
            <div class="flex flex-col ${idx % 2 === 0 ? 'lg:flex-row' : 'lg:flex-row-reverse'} gap-12 items-center">
              <div class="w-full lg:w-1/2 relative h-[400px] border border-zinc-800 p-2 bg-zinc-900 rounded-[2rem] shadow-2xl">
                <div class="relative w-full h-full overflow-hidden rounded-2xl">
                  <img src="${story.img}" alt="${story.title}" class="w-full h-full object-cover grayscale hover:grayscale-0 transition-all duration-700">
                </div>
                <div class="absolute -bottom-6 -right-6 bg-morris-blue p-6 shadow-xl hidden md:block rounded-xl">
                  <div class="text-white font-black uppercase tracking-widest text-sm">${story.metric}</div>
                </div>
              </div>
              <div class="w-full lg:w-1/2">
                <h3 class="text-morris-red font-bold text-sm tracking-[0.2em] uppercase mb-4">${story.client}</h3>
                <h2 class="text-3xl md:text-4xl font-black uppercase tracking-tight text-white mb-6">${story.title}</h2>
                <p class="text-zinc-400 text-lg leading-relaxed mb-8">${story.desc}</p>
                <button class="flex items-center text-sm font-bold uppercase tracking-widest text-white hover:text-morris-blue transition-colors group">
                  Read Full Study <i data-lucide="arrow-right" class="ml-2 w-4 h-4 group-hover:translate-x-1 transition-transform"></i>
                </button>
              </div>
            </div>
      `).join('');

      return `
        <div class="pt-20">
          <section class="pt-32 pb-16 bg-zinc-950 border-b border-zinc-900">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
              <h1 class="text-5xl md:text-7xl font-black text-white uppercase tracking-tighter mb-6">Success Stories</h1>
              <p class="text-xl text-zinc-400 max-w-3xl leading-relaxed">
                Case studies demonstrating our capacity to handle the most demanding logistical challenges across the energy, manufacturing, and defense sectors.
              </p>
            </div>
          </section>
          <section class="py-24 bg-zinc-950">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-32">
              ${storiesHtml}
            </div>
          </section>
        </div>
      `;
    }

    '''
text = text[:start_about] + success_stories_code + text[start_about:]

# 3. Update renderPage routing
text = text.replace("} else if (hash === '#/about-us') {", "} else if (hash === '#/success-stories') { content.innerHTML = renderSuccessStories(); } else if (hash === '#/about-us') {")

# 4. Replace DOMContentLoaded navLinks rendering
start_dom = text.find("navLinks.forEach(link => {")
end_dom = text.find("// Mobile menu toggle", start_dom)

new_dom = '''navLinks.forEach(link => {
        // Desktop Link
        const a = document.createElement('a');
        a.href = link.path;
        a.className = 'text-sm font-bold text-zinc-300 hover:text-white uppercase tracking-widest transition-colors nav-modern';
        a.textContent = link.name;
        navLinksContainer.appendChild(a);

        // Mobile Link
        const mobileA = document.createElement('a');
        mobileA.href = link.path;
        mobileA.className = 'block px-4 py-4 border-b border-zinc-900 text-sm font-bold uppercase tracking-widest text-zinc-400 hover:text-white transition-colors';
        mobileA.textContent = link.name;
        mobileA.onclick = () => {
          document.getElementById('mobile-menu').classList.add('hidden');
        };
        mobileNavLinksContainer.appendChild(mobileA);
      });

      // Add Portal Login button to desktop
      const portalBtn = document.createElement('a');
      portalBtn.href = '#/customer-center';
      portalBtn.className = 'bg-morris-red hover:bg-red-700 text-white px-6 py-2.5 font-bold text-sm uppercase tracking-widest transition-all rounded-sm ml-4 btn-modern';
      portalBtn.textContent = 'Portal Login';
      navLinksContainer.appendChild(portalBtn);

      // Add Portal Login button to mobile
      const mobilePortalBtn = document.createElement('a');
      mobilePortalBtn.href = '#/customer-center';
      mobilePortalBtn.className = 'block w-full text-center bg-morris-red text-white py-4 font-bold uppercase tracking-widest mt-6 rounded-sm btn-modern';
      mobilePortalBtn.textContent = 'Portal Login';
      mobilePortalBtn.onclick = () => {
        document.getElementById('mobile-menu').classList.add('hidden');
      };
      mobileNavLinksContainer.appendChild(mobilePortalBtn);

      '''
text = text[:start_dom] + new_dom + text[end_dom:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated nav structure!")
