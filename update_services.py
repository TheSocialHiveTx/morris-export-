import sys
import re

file_path = r'c:\Users\suppo\OneDrive\Desktop\Developer\morris-export-\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('function renderServicesHub() {')
end_idx = content.find('function renderServiceDetail(slug) {')

if start_idx != -1 and end_idx != -1:
    render_hub_new = '''function renderServicesHub() {
      const categories = ['Packing & Crating', 'Logistics & Transport', 'Storage & Management', 'Technology'];

      const categorySections = categories.map(cat => {
        const catServices = SERVICES.filter(s => s.category === cat);
        const catIcon = { 'Packing & Crating': 'box', 'Logistics & Transport': 'truck', 'Storage & Management': 'warehouse', 'Technology': 'cpu' }[cat] || 'layers';
        return `
          <div class="mb-24">
            <div class="flex items-center gap-4 mb-12 pb-4 border-b border-zinc-200">
              <div class="w-12 h-12 bg-blue-100 text-morris-blue rounded-xl flex items-center justify-center flex-shrink-0 shadow-inner">
                <i data-lucide="${catIcon}" class="w-6 h-6"></i>
              </div>
              <h2 class="text-3xl font-black uppercase tracking-tight text-zinc-900">${cat}</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              ${catServices.map(service => `
                <a href="#/services/${service.slug}" class="group bg-white rounded-3xl border border-zinc-100 hover:border-blue-500/30 transition-all duration-300 shadow-sm hover:shadow-2xl overflow-hidden flex flex-col transform hover:-translate-y-2">
                  <div class="relative h-56 overflow-hidden">
                    <img src="${service.coverImg}" alt="${service.title}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
                    <div class="absolute top-4 right-4 w-10 h-10 bg-white/20 backdrop-blur-md text-white rounded-xl flex items-center justify-center border border-white/30 shadow-lg">
                      <i data-lucide="${service.icon}" class="w-5 h-5"></i>
                    </div>
                  </div>
                  <div class="p-8 flex flex-col flex-1">
                    <h3 class="text-xl font-bold mb-3 text-zinc-900 group-hover:text-morris-blue transition-colors">${service.title}</h3>
                    <p class="text-zinc-500 text-sm mb-6 leading-relaxed flex-1">${service.description}</p>
                    <div class="flex items-center justify-between pt-5 border-t border-zinc-100 mt-auto">
                      <div class="flex gap-2 flex-wrap">
                        ${(service.keyBenefits || []).slice(0, 2).map(b => `<span class="text-[10px] bg-blue-50 text-blue-700 font-bold uppercase tracking-widest px-3 py-1 rounded-full">${b}</span>`).join('')}
                      </div>
                      <div class="w-8 h-8 rounded-full bg-zinc-50 group-hover:bg-blue-50 flex items-center justify-center transition-colors">
                        <i data-lucide="arrow-right" class="w-4 h-4 text-zinc-400 group-hover:text-morris-blue transition-colors"></i>
                      </div>
                    </div>
                  </div>
                </a>
              `).join('')}
            </div>
          </div>
        `;
      }).join('');

      return `
        <div class="pt-20">
          <!-- Services Hero -->
          <section class="relative h-[60vh] overflow-hidden flex items-center">
            <div class="absolute inset-0 z-0">
                <img src="images/warehousemanagement/warehousepackaging2.webp" alt="Services" class="w-full h-full object-cover scale-105 animate-[pulse_15s_ease-in-out_infinite]">
                <div class="absolute inset-0 bg-gradient-to-r from-slate-900/90 to-transparent"></div>
            </div>
            <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full pt-12">
              <nav class="text-white/60 text-sm mb-6 flex items-center gap-2 font-medium tracking-wide">
                <a href="#/" class="hover:text-white transition-colors">HOME</a>
                <i data-lucide="chevron-right" class="w-3 h-3"></i>
                <span class="text-white">SERVICES</span>
              </nav>
              <h1 class="text-5xl md:text-7xl font-black text-white uppercase tracking-tighter leading-none mb-6 drop-shadow-md">Our Services</h1>
              <p class="text-xl text-blue-100 max-w-2xl leading-relaxed">End-to-end export packing, crating, logistics, and storage — engineered for global transit.</p>
            </div>
          </section>

          <!-- Stats Bar -->
          <section class="bg-morris-blue text-white relative z-20 shadow-2xl -mt-8 mx-4 md:mx-auto max-w-7xl rounded-2xl overflow-hidden">
            <div class="grid grid-cols-2 md:grid-cols-4 divide-y md:divide-y-0 md:divide-x divide-blue-400/30">
              ${[
                { val: '80+', label: 'Years in Business' },
                { val: '250K+', label: 'Sq Ft of Storage' },
                { val: '140K', label: 'Max Lift Capacity (lbs)' },
                { val: '12+', label: 'Specialized Services' }
              ].map(s => `
                <div class="py-10 px-6 text-center hover:bg-blue-700/50 transition-colors">
                  <div class="text-4xl font-black mb-2">${s.val}</div>
                  <div class="text-blue-200 text-xs font-bold uppercase tracking-widest">${s.label}</div>
                </div>
              `).join('')}
            </div>
          </section>

          <!-- Category Sections -->
          <section class="bg-zinc-50 pt-32 pb-20 -mt-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
              ${categorySections}
            </div>
          </section>

          <!-- CTA -->
          <section class="bg-zinc-900 py-24 text-center">
            <div class="max-w-4xl mx-auto px-4">
              <h2 class="text-4xl font-black text-white uppercase mb-6 tracking-tight">Ready to get started?</h2>
              <p class="text-zinc-400 mb-10 text-xl leading-relaxed">Tell us about your project and our team will develop a custom solution for your cargo.</p>
              <a href="#/contact-us" class="inline-block bg-morris-red text-white px-12 py-5 rounded-xl font-bold uppercase tracking-widest hover:bg-red-700 transition-all shadow-xl shadow-red-900/40">Request a Quote</a>
            </div>
          </section>
        </div>
      `;
    }
'''
    content = content[:start_idx] + render_hub_new + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated Services Hub')
