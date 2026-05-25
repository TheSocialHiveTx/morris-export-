import sys
import re

file_path = r'c:\Users\suppo\OneDrive\Desktop\Developer\morris-export-\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Head
head_old = '''  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap"
    rel="stylesheet">
  <style>'''

head_new = '''  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            'morris-blue': '#005bb5',
            'morris-red': '#cc0f1f',
          },
          fontFamily: {
            sans: ['Inter', 'sans-serif'],
          }
        }
      }
    }
  </script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>'''

content = content.replace(head_old, head_new)

# 2. Update body background
body_old = '''    body {
      font-family: 'Inter', ui-sans-serif, system-ui, sans-serif;
      background:
        radial-gradient(1000px 500px at 10% -10%, rgba(0, 120, 212, 0.06), transparent 60%),
        radial-gradient(900px 450px at 90% -20%, rgba(232, 17, 35, 0.05), transparent 60%),
        #ffffff;
      scroll-behavior: smooth;
    }'''
    
body_new = '''    body {
      font-family: 'Inter', ui-sans-serif, system-ui, sans-serif;
      background:
        radial-gradient(1000px 500px at 10% -10%, rgba(0, 91, 181, 0.08), transparent 60%),
        radial-gradient(900px 450px at 90% -20%, rgba(204, 15, 31, 0.05), transparent 60%),
        #f8fafc;
      scroll-behavior: smooth;
    }'''

content = content.replace(body_old, body_new)

# 3. Update Navbar
nav_old = '''  <nav class="fixed w-full z-50 bg-white/95 backdrop-blur-md border-b border-zinc-200 modern-nav">'''
nav_new = '''  <nav class="fixed w-full z-50 bg-white/70 backdrop-blur-xl border-b border-white/40 shadow-[0_4px_30px_rgba(0,0,0,0.1)] modern-nav">'''
content = content.replace(nav_old, nav_new)

# 4. Update Footer
footer_old = '''  <footer class="bg-zinc-900 text-zinc-400 py-16">'''
footer_new = '''  <footer class="bg-gradient-to-b from-zinc-900 to-black text-zinc-400 py-16 border-t border-zinc-800">'''
content = content.replace(footer_old, footer_new)

# 5. Replace renderHome
start_idx = content.find('function renderHome() {')
end_idx = content.find('function renderAbout() {')

if start_idx != -1 and end_idx != -1:
    render_home_new = '''function renderHome() {
      const servicesGridHtml = SERVICES.slice(0, 8).map(s => `
                <a href="#/services/${s.slug}" class="service-tile group rounded-2xl overflow-hidden shadow-sm hover:shadow-2xl transition-all duration-500 transform hover:-translate-y-2 bg-white border border-white/20">
                    <div class="relative h-48 md:h-64 overflow-hidden">
                        <img src="${s.coverImg}" alt="${s.title}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
                        <div class="absolute bottom-4 left-6 right-6">
                            <h3 class="text-white font-black text-xl tracking-tight mb-1">${s.title}</h3>
                            <div class="w-12 h-1 bg-morris-red transform origin-left transition-all duration-300 group-hover:w-full"></div>
                        </div>
                    </div>
                </a>
            `).join('');

      return `
                <div class="pt-20">
                    <!-- Hero Section -->
                    <section class="min-h-[85vh] relative overflow-hidden flex items-center">
                        <div class="absolute inset-0 z-0">
                            <img src="images/warehousemanagement/warehousepackaging2.webp" alt="Hero" class="w-full h-full object-cover scale-105 animate-[pulse_20s_ease-in-out_infinite]">
                            <div class="absolute inset-0 bg-gradient-to-r from-slate-900/90 via-slate-900/70 to-transparent"></div>
                        </div>
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full pt-12 pb-24">
                            <div class="max-w-3xl">
                                <span class="inline-block py-1 px-3 rounded-full bg-blue-500/20 text-blue-300 font-semibold text-sm mb-6 border border-blue-500/30 backdrop-blur-md">Established 1942</span>
                                <h1 class="text-5xl md:text-7xl font-black text-white uppercase leading-[1.1] tracking-tighter mb-6 drop-shadow-lg">
                                    Engineered For <br><span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-blue-200">Global Transit</span>
                                </h1>
                                <p class="text-lg md:text-xl text-slate-300 mb-10 max-w-2xl leading-relaxed">
                                    Comprehensive logistics and transportation solutions. From field export packing and custom crating to heavy-haul trucking and warehousing.
                                </p>
                                <div class="flex flex-col sm:flex-row gap-4">
                                    <a href="#/services" class="btn-modern bg-morris-red text-white py-4 px-8 rounded-xl font-bold uppercase tracking-widest text-center hover:bg-red-700 transition-colors shadow-lg shadow-red-900/50">Explore Services</a>
                                    <a href="#/contact-us" class="btn-modern bg-white/10 backdrop-blur-md border border-white/20 text-white py-4 px-8 rounded-xl font-bold uppercase tracking-widest text-center hover:bg-white/20 transition-colors">Get a Quote</a>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Service Grid Section -->
                    <section class="bg-zinc-50 py-24 relative">
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                            <div class="flex flex-col md:flex-row justify-between items-end mb-12">
                                <div>
                                    <h3 class="text-morris-blue font-bold tracking-widest uppercase mb-2">Our Capabilities</h3>
                                    <h2 class="text-4xl font-black text-zinc-900 uppercase tracking-tight">Featured Services</h2>
                                </div>
                                <a href="#/services" class="mt-4 md:mt-0 text-morris-red font-bold flex items-center hover:text-red-700 transition-colors">
                                    View all services <i data-lucide="arrow-right" class="w-5 h-5 ml-2"></i>
                                </a>
                            </div>
                            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                                ${servicesGridHtml}
                            </div>
                        </div>
                    </section>

                    <!-- Modern Stats / Info Section -->
                    <section class="py-24 bg-white border-t border-zinc-100">
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                                <div class="relative h-[600px] rounded-3xl overflow-hidden shadow-2xl">
                                    <img src="images/onsitepacking/onsitepacking2.webp" class="w-full h-full object-cover" alt="Industrial Operations">
                                    <div class="absolute inset-0 bg-gradient-to-t from-morris-blue/80 to-transparent flex items-end p-10">
                                        <div class="text-white">
                                            <div class="text-5xl font-black mb-2">80+</div>
                                            <div class="text-lg font-medium text-blue-100 uppercase tracking-widest">Years of Excellence</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="space-y-8">
                                    <h2 class="text-4xl font-black text-zinc-900 uppercase tracking-tight leading-tight">
                                        Why Choose <br><span class="text-morris-blue">Morris Export?</span>
                                    </h2>
                                    <p class="text-lg text-zinc-600 leading-relaxed">
                                        With a commitment to excellence and customer satisfaction spanning more than 80 years, we are the partner you can trust to ensure your imports and exports reach their destination safely.
                                    </p>
                                    
                                    <div class="space-y-6 mt-8">
                                        <div class="flex items-start bg-zinc-50 p-6 rounded-2xl border border-zinc-100">
                                            <div class="w-12 h-12 bg-blue-100 text-morris-blue rounded-xl flex items-center justify-center shrink-0 mr-5">
                                                <i data-lucide="shield" class="w-6 h-6"></i>
                                            </div>
                                            <div>
                                                <h4 class="text-xl font-bold text-zinc-900 mb-2">Wrap Protection</h4>
                                                <p class="text-zinc-600 text-sm">Protective layering prevents damage during transportation, ideal for delicate or fragile shipments.</p>
                                            </div>
                                        </div>
                                        <div class="flex items-start bg-zinc-50 p-6 rounded-2xl border border-zinc-100">
                                            <div class="w-12 h-12 bg-red-100 text-morris-red rounded-xl flex items-center justify-center shrink-0 mr-5">
                                                <i data-lucide="map-pin" class="w-6 h-6"></i>
                                            </div>
                                            <div>
                                                <h4 class="text-xl font-bold text-zinc-900 mb-2">Onsite Export Packing</h4>
                                                <p class="text-zinc-600 text-sm">We send professionals to your facilities to package and prepare products too large for a standard packaging facility.</p>
                                            </div>
                                        </div>
                                        <div class="flex items-start bg-zinc-50 p-6 rounded-2xl border border-zinc-100">
                                            <div class="w-12 h-12 bg-blue-100 text-morris-blue rounded-xl flex items-center justify-center shrink-0 mr-5">
                                                <i data-lucide="warehouse" class="w-6 h-6"></i>
                                            </div>
                                            <div>
                                                <h4 class="text-xl font-bold text-zinc-900 mb-2">Warehouse Management</h4>
                                                <p class="text-zinc-600 text-sm">State-of-the-art facility equipped with the latest technology for safe storage and inventory transparency.</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- CTA Section -->
                    <section class="relative py-32 overflow-hidden">
                        <img src="images/trucking/Screenshot 2026-03-19 091824.png" alt="CTA BG" class="absolute inset-0 w-full h-full object-cover">
                        <div class="absolute inset-0 bg-gradient-to-b from-black/80 to-black/60 backdrop-blur-sm"></div>
                        <div class="relative max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                            <h2 class="text-5xl font-black text-white uppercase mb-6 tracking-tighter">Ready to Ship?</h2>
                            <p class="text-xl text-slate-300 mb-10 max-w-2xl mx-auto">Get in touch with our experts today and discover how we can optimize your global logistics.</p>
                            <a href="#/contact-us" class="inline-block bg-morris-red hover:bg-red-700 text-white py-5 px-14 rounded-xl font-bold uppercase tracking-widest transition-all shadow-xl shadow-red-900/30 transform hover:-translate-y-1">
                                Contact Us Today
                            </a>
                        </div>
                    </section>
                </div>
            `;
    }
'''
    content = content[:start_idx] + render_home_new + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html')
