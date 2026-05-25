import sys
import re

file_path = r'c:\Users\suppo\OneDrive\Desktop\Developer\morris-export-\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('function renderAbout() {')
end_idx = content.find('function renderServicesHub() {')

if start_idx != -1 and end_idx != -1:
    render_about_new = '''function renderAbout() {
      return `
                <div class="pt-20">
                    <!-- About Sub-Header -->
                    <section class="relative h-[50vh] flex items-center overflow-hidden">
                        <div class="absolute inset-0 z-0">
                            <img src="images/facilitiesstorage/Screenshot 2026-03-19 091959.png" class="w-full h-full object-cover scale-105 animate-[pulse_20s_ease-in-out_infinite]" alt="Morris Export Facility">
                            <div class="absolute inset-0 bg-gradient-to-r from-black/80 via-black/50 to-transparent"></div>
                        </div>
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full pt-10">
                            <div class="flex items-center gap-4 mb-6">
                                <img src="images/Screenshot 2026-03-19 103621.png" alt="Logo" class="h-12 w-auto brightness-0 invert opacity-90">
                            </div>
                            <h1 class="text-5xl md:text-7xl font-black text-white uppercase tracking-tighter mb-4 drop-shadow-lg">About Us</h1>
                            <div class="w-24 h-1.5 bg-morris-red mb-6"></div>
                            <h2 class="text-2xl md:text-3xl font-medium text-blue-100 uppercase tracking-widest max-w-2xl">Packing The World Since 1942</h2>
                        </div>
                    </section>

                    <!-- Main Biography Section -->
                    <section class="bg-zinc-50 py-24 relative overflow-hidden">
                        <div class="absolute top-0 right-0 w-1/2 h-full bg-white/50 backdrop-blur-3xl transform skew-x-12 -z-10 translate-x-1/4"></div>
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                            <div class="grid grid-cols-1 lg:grid-cols-2 gap-20 items-center">
                                <div class="relative">
                                    <div class="absolute inset-0 bg-morris-blue rounded-3xl transform translate-x-4 translate-y-4"></div>
                                    <div class="rounded-3xl overflow-hidden shadow-2xl relative z-10 border border-zinc-200 bg-white p-2">
                                        <img src="images/team/rayvargas.webp" alt="Historical Experience" class="w-full h-auto object-cover rounded-2xl">
                                    </div>
                                    
                                    <!-- Floating badge -->
                                    <div class="absolute -bottom-8 -left-8 bg-white p-6 rounded-2xl shadow-2xl border border-zinc-100 z-20 flex items-center gap-4 animate-[floatAura_8s_ease-in-out_infinite]">
                                        <div class="w-16 h-16 bg-blue-50 text-morris-blue rounded-xl flex items-center justify-center">
                                            <i data-lucide="award" class="w-8 h-8"></i>
                                        </div>
                                        <div>
                                            <div class="text-3xl font-black text-zinc-900 leading-none mb-1">80+</div>
                                            <div class="text-xs font-bold text-zinc-500 uppercase tracking-widest">Years Expertise</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="space-y-8">
                                    <div>
                                        <h3 class="text-sm font-bold text-morris-blue uppercase tracking-widest mb-3">Our Heritage</h3>
                                        <h2 class="text-4xl font-black text-zinc-900 uppercase tracking-tight leading-tight">Morris Export Services</h2>
                                    </div>
                                    
                                    <div class="prose prose-lg text-zinc-600 prose-p:leading-relaxed">
                                        <p>
                                            Steeped in history, dating back to our establishment in 1942, we have successfully blended old world craftsmanship, while utilizing today’s modern technology to generate the best service in the packing industry.
                                        </p>
                                        <p>
                                            Morris Export is able to lead industry standards by having the most experienced employees in the packing industry. With almost 80 years of experience in the packing industry, we’ve gained the knowledge and craftsmanship no other packer can compete with.
                                        </p>
                                        <p>
                                            Essential to our process, we also pride ourselves on our software and technological development. Our proprietary software, which works with any ERP system, gives you full transparency of our entire packing process. We encourage you to have full access to our shared system!
                                        </p>
                                    </div>
                                    
                                    <div class="pt-6 border-t border-zinc-200">
                                        <a href="#/contact-us" class="inline-flex items-center font-bold text-lg text-morris-blue hover:text-blue-800 transition-colors group">
                                            Contact us to see how our software integration can help you
                                            <i data-lucide="arrow-right" class="w-5 h-5 ml-2 transform group-hover:translate-x-1 transition-transform"></i>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Sales Presentation Section -->
                    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
                        <div class="flex flex-col md:flex-row overflow-hidden rounded-[2.5rem] shadow-2xl border border-zinc-100 bg-white">
                            <!-- Left: CTA Area -->
                            <div class="w-full md:w-5/12 bg-zinc-900 p-12 md:p-16 flex flex-col justify-center relative overflow-hidden">
                                <div class="absolute top-0 right-0 w-64 h-64 bg-white opacity-5 rounded-full blur-3xl transform translate-x-1/2 -translate-y-1/2"></div>
                                <h3 class="text-3xl font-black text-white uppercase mb-6 leading-tight relative z-10">
                                    For more information watch our <span class="text-morris-red">Sales Presentation</span>
                                </h3>
                                <p class="text-zinc-400 text-base mb-10 relative z-10">
                                    Please click ‘Save’ to save the presentation to your computer before opening.
                                </p>
                                <div class="flex flex-col sm:flex-row gap-4 relative z-10">
                                    <button class="bg-morris-red hover:bg-red-700 text-white py-4 px-8 rounded-xl font-bold uppercase tracking-widest flex items-center justify-center gap-3 transition-all shadow-lg shadow-red-900/40">
                                        <i data-lucide="play" class="w-5 h-5 fill-current"></i> WATCH
                                    </button>
                                    <button class="bg-white/10 hover:bg-white/20 text-white py-4 px-8 rounded-xl font-bold uppercase tracking-widest flex items-center justify-center gap-3 transition-all border border-white/10">
                                        <i data-lucide="download" class="w-5 h-5"></i> SAVE
                                    </button>
                                </div>
                            </div>
                            <!-- Right: Visual Background -->
                            <div class="w-full md:w-7/12 relative min-h-[400px]">
                                <img src="images/team/rayvargas.webp" alt="Historical Presentation" class="w-full h-full object-cover">
                                <div class="absolute inset-0 bg-gradient-to-r from-zinc-900 via-transparent to-transparent opacity-80 md:opacity-100"></div>
                                <div class="absolute inset-0 bg-black/20 group cursor-pointer flex items-center justify-center">
                                    <div class="w-24 h-24 bg-white/20 backdrop-blur-md border border-white/30 text-white rounded-full flex items-center justify-center shadow-[0_0_50px_rgba(255,255,255,0.2)] transform transition-all duration-500 group-hover:scale-110 group-hover:bg-white group-hover:text-morris-red">
                                        <i data-lucide="play" class="w-10 h-10 fill-current ml-1"></i>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Bottom Nav Extension (Matching Reference) -->
                    <section class="bg-zinc-100 py-16 border-t border-zinc-200">
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center uppercase">
                            <div class="flex flex-wrap justify-center gap-x-8 gap-y-4 text-sm font-bold text-zinc-500 mb-8 tracking-widest">
                                <a href="#/" class="hover:text-morris-blue transition-colors">Home</a>
                                <a href="#/about-us" class="text-morris-blue">About Us</a>
                                <a href="#/facilities" class="hover:text-morris-blue transition-colors">Facilities</a>
                                <a href="#/customer-center" class="hover:text-morris-blue transition-colors">Customer Center</a>
                                <a href="#/contact-us" class="hover:text-morris-blue transition-colors">Contact Us</a>
                                <a href="/sitemap.xml" target="_blank" class="hover:text-morris-blue transition-colors">XML Sitemap</a>
                                <a href="#/html-sitemap" class="hover:text-morris-blue transition-colors">HTML Sitemap</a>
                            </div>
                            <p class="text-xs text-zinc-400 font-medium tracking-widest">© 2026, Morris Export Services, Inc. All Rights Reserved.</p>
                        </div>
                    </section>
                </div>
            `;
    }
'''
    content = content[:start_idx] + render_about_new + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated About')
