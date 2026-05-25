import sys
import re

file_path = r'c:\Users\suppo\OneDrive\Desktop\Developer\morris-export-\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Facilities
start_fac = content.find('function renderFacilities() {')
end_fac = content.find('function renderCustomerCenter() {')

fac_new = '''function renderFacilities() {
      return `
                <div class="pt-20">
                    <section class="relative h-[40vh] flex items-center overflow-hidden">
                        <div class="absolute inset-0 z-0">
                            <img src="images/facilitiesstorage/Secure Facilities.webp" class="w-full h-full object-cover scale-105 animate-[pulse_20s_ease-in-out_infinite]" alt="Facility Background">
                            <div class="absolute inset-0 bg-gradient-to-r from-slate-900/90 to-transparent"></div>
                        </div>
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full pt-10">
                            <h1 class="text-5xl md:text-7xl font-black text-white uppercase tracking-tighter mb-4 drop-shadow-lg">Our Facilities</h1>
                            <div class="w-24 h-1.5 bg-morris-red mb-6"></div>
                            <h2 class="text-xl md:text-2xl font-medium text-blue-100 max-w-2xl">Strategic Storage & Warehousing Engineered for Global Transit.</h2>
                        </div>
                    </section>

                    <section class="py-24 bg-zinc-50 relative -mt-10 z-20 rounded-t-[3rem] shadow-2xl">
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
                                <div class="bg-white p-10 md:p-14 rounded-[2.5rem] border border-zinc-100 shadow-xl relative overflow-hidden">
                                    <div class="absolute top-0 right-0 w-32 h-32 bg-blue-50 rounded-bl-[5rem] -z-10"></div>
                                    <div class="w-16 h-16 bg-blue-100 text-morris-blue rounded-2xl flex items-center justify-center mb-8 shadow-sm">
                                        <i data-lucide="warehouse" class="w-8 h-8"></i>
                                    </div>
                                    <h2 class="text-3xl font-black text-zinc-900 mb-6 uppercase tracking-tight">Scale & Security</h2>
                                    <p class="text-lg text-zinc-600 mb-8 leading-relaxed">
                                        Our facilities offer over <strong class="text-morris-blue">250,000 square feet</strong> of indoor storage and extensive outdoor laydown areas, all secured and monitored 24/7.
                                    </p>
                                    <ul class="space-y-5">
                                        <li class="flex items-start">
                                            <div class="w-6 h-6 bg-blue-100 text-morris-blue rounded-full flex items-center justify-center shrink-0 mr-4 mt-1"><i data-lucide="check" class="w-3 h-3"></i></div>
                                            <span class="text-zinc-700 font-medium">Climate-controlled options for sensitive cargo</span>
                                        </li>
                                        <li class="flex items-start">
                                            <div class="w-6 h-6 bg-blue-100 text-morris-blue rounded-full flex items-center justify-center shrink-0 mr-4 mt-1"><i data-lucide="check" class="w-3 h-3"></i></div>
                                            <span class="text-zinc-700 font-medium">Heavy-lift capabilities (up to 140K lbs)</span>
                                        </li>
                                        <li class="flex items-start">
                                            <div class="w-6 h-6 bg-blue-100 text-morris-blue rounded-full flex items-center justify-center shrink-0 mr-4 mt-1"><i data-lucide="check" class="w-3 h-3"></i></div>
                                            <span class="text-zinc-700 font-medium">Real-time inventory management via M-Pact</span>
                                        </li>
                                    </ul>
                                </div>
                                <div class="relative h-[600px] rounded-[2.5rem] overflow-hidden shadow-2xl border border-white/20 group">
                                    <img src="images/facilitiesstorage/Secure Facilities1.webp" alt="Facility Overview" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
                                    <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
                                    <div class="absolute bottom-10 left-10 right-10">
                                        <div class="bg-white/10 backdrop-blur-md border border-white/20 rounded-2xl p-6 text-white">
                                            <div class="text-3xl font-black mb-1">24/7</div>
                                            <div class="text-sm font-bold uppercase tracking-widest text-blue-200">Monitored Security</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                </div>
            `;
    }
'''
if start_fac != -1 and end_fac != -1:
    content = content[:start_fac] + fac_new + content[end_fac:]

# 2. Update Customer Center
start_cust = content.find('function renderCustomerCenter() {')
end_cust = content.find('function renderContact() {')

cust_new = '''function renderCustomerCenter() {
      return `
                <div class="pt-20">
                    <section class="relative h-[40vh] flex items-center overflow-hidden">
                        <div class="absolute inset-0 z-0">
                            <img src="images/warehousemanagement/warehousepackaging1.webp" class="w-full h-full object-cover scale-105 animate-[pulse_20s_ease-in-out_infinite]" alt="Customer Center Background">
                            <div class="absolute inset-0 bg-gradient-to-r from-morris-blue/90 to-slate-900/90 mix-blend-multiply"></div>
                        </div>
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full pt-10 text-center">
                            <div class="inline-flex items-center justify-center w-20 h-20 bg-white/10 backdrop-blur-md border border-white/20 rounded-full mb-6">
                                <i data-lucide="users" class="w-8 h-8 text-white"></i>
                            </div>
                            <h1 class="text-5xl md:text-7xl font-black text-white uppercase tracking-tighter mb-4 drop-shadow-lg">Customer Center</h1>
                            <p class="text-xl md:text-2xl font-medium text-blue-100 max-w-2xl mx-auto">Portals, resources, and applications to keep your logistics flowing.</p>
                        </div>
                    </section>

                    <section class="py-24 bg-zinc-50 relative -mt-10 z-20 rounded-t-[3rem] shadow-2xl">
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                                <a href="https://webstars.morris-export.com" target="_blank" rel="noopener noreferrer" class="group bg-zinc-900 border border-zinc-800 p-10 rounded-[2rem] hover:-translate-y-2 transition-all duration-300 shadow-xl hover:shadow-2xl flex flex-col justify-between">
                                    <div>
                                        <div class="w-16 h-16 bg-morris-blue text-white rounded-2xl flex items-center justify-center mb-8">
                                            <i data-lucide="external-link" class="w-8 h-8"></i>
                                        </div>
                                        <h3 class="text-2xl font-black text-white uppercase tracking-tight mb-4 group-hover:text-morris-blue transition-colors">Customer Reports</h3>
                                        <p class="text-zinc-400 leading-relaxed">Access your real-time tracking, receiving documentation, and inventory reports via our secure Webstars portal.</p>
                                    </div>
                                    <div class="mt-8 pt-6 border-t border-zinc-800 flex items-center text-sm font-bold uppercase tracking-widest text-morris-blue">
                                        Login Now <i data-lucide="arrow-right" class="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform"></i>
                                    </div>
                                </a>

                                <a href="#/credit-application" class="group bg-white border border-zinc-200 p-10 rounded-[2rem] hover:-translate-y-2 transition-all duration-300 shadow-sm hover:shadow-xl flex flex-col justify-between">
                                    <div>
                                        <div class="w-16 h-16 bg-blue-50 text-morris-blue rounded-2xl flex items-center justify-center mb-8">
                                            <i data-lucide="clipboard-list" class="w-8 h-8"></i>
                                        </div>
                                        <h3 class="text-2xl font-black text-zinc-900 uppercase tracking-tight mb-4 group-hover:text-morris-blue transition-colors">Credit Application</h3>
                                        <p class="text-zinc-600 leading-relaxed">Establish an account with us. Quickly fill out our digital credit application to begin our partnership.</p>
                                    </div>
                                    <div class="mt-8 pt-6 border-t border-zinc-100 flex items-center text-sm font-bold uppercase tracking-widest text-morris-blue">
                                        Apply Now <i data-lucide="arrow-right" class="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform"></i>
                                    </div>
                                </a>

                                <a href="#/faq" class="group bg-white border border-zinc-200 p-10 rounded-[2rem] hover:-translate-y-2 transition-all duration-300 shadow-sm hover:shadow-xl flex flex-col justify-between">
                                    <div>
                                        <div class="w-16 h-16 bg-blue-50 text-morris-blue rounded-2xl flex items-center justify-center mb-8">
                                            <i data-lucide="help-circle" class="w-8 h-8"></i>
                                        </div>
                                        <h3 class="text-2xl font-black text-zinc-900 uppercase tracking-tight mb-4 group-hover:text-morris-blue transition-colors">FAQ</h3>
                                        <p class="text-zinc-600 leading-relaxed">Have a question about NCB inspections, bonded facilities, or receiving hours? Find your answers here.</p>
                                    </div>
                                    <div class="mt-8 pt-6 border-t border-zinc-100 flex items-center text-sm font-bold uppercase tracking-widest text-morris-blue">
                                        Read FAQs <i data-lucide="arrow-right" class="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform"></i>
                                    </div>
                                </a>
                            </div>
                        </div>
                    </section>
                </div>
            `;
    }
'''
if start_cust != -1 and end_cust != -1:
    content = content[:start_cust] + cust_new + content[end_cust:]

# 3. Update FAQ & Team & Credit App
# To be safe, I'll update Team first since it's the one the user was specifically looking at.
start_team = content.find('function renderOurTeam() {')
end_team = content.find('function renderTerms() {')

team_new = '''function renderOurTeam() {
      const teamMembers = [
        { name: 'Andrew Talley', email: 'ATalley@morrisexport.com', phone: '(713) 672-5411', cell: '', title: 'CEO', image: 'images/Screenshot 2026-03-19 103621.png' },
        { name: 'Gary Baumbach', email: 'gbaumbach@morrisexport.com', phone: '(713) 672-5425', cell: '', title: 'Treasurer & CFO', image: 'images/Screenshot 2026-03-19 103621.png' },
        { name: 'Herbie Garza', email: 'HGarza@morrisexport.com', phone: '(713) 672-5428', cell: '(713) 907-4983', title: 'Sales', image: 'images/Screenshot 2026-03-19 103621.png' },
        { name: 'Kim Solomon', email: 'ksolomon@morrisexport.com', phone: '(713) 672-5443', cell: '', title: 'Account Coordinator', image: 'images/team/kimsolomon.webp' },
        { name: 'Lisa Allen', email: 'LAllen@morrisexport.com', phone: '(713) 672-5436', cell: '', title: 'Account Coordinator', image: 'images/team/lisaallen.webp' },
        { name: 'Ray Vargas', email: 'rvargas@morrisexport.com', phone: '(713) 672-5484', cell: '', title: 'Operations Manager', image: 'images/team/rayvargas.webp' }
      ];

      const teamHtml = teamMembers.map(member => `
                <article class="bg-white rounded-[2rem] border border-zinc-100 shadow-lg hover:shadow-2xl transition-all duration-500 overflow-hidden group transform hover:-translate-y-2">
                    <div class="h-32 bg-zinc-900 relative">
                        <div class="absolute inset-0 bg-gradient-to-r from-morris-blue/20 to-transparent"></div>
                        <div class="absolute -bottom-12 left-8 w-24 h-24 rounded-2xl border-4 border-white overflow-hidden bg-white shadow-xl z-10 group-hover:scale-110 transition-transform duration-500">
                            <img src="${member.image}" alt="${member.name}" class="w-full h-full object-cover">
                        </div>
                    </div>
                    <div class="pt-16 pb-8 px-8">
                        <div class="text-xs font-bold text-morris-blue uppercase tracking-widest mb-1">${member.title}</div>
                        <h3 class="text-2xl font-black text-zinc-900 uppercase tracking-tight mb-4">${member.name}</h3>
                        
                        <div class="space-y-3 pt-4 border-t border-zinc-100">
                            <div class="flex items-center text-zinc-600 text-sm">
                                <i data-lucide="mail" class="w-4 h-4 mr-3 text-zinc-400"></i>
                                <a href="mailto:${member.email}" class="hover:text-morris-blue transition-colors truncate">${member.email}</a>
                            </div>
                            <div class="flex items-center text-zinc-600 text-sm">
                                <i data-lucide="phone" class="w-4 h-4 mr-3 text-zinc-400"></i>
                                <a href="tel:${member.phone.replace(/[^0-9]/g, '')}" class="hover:text-morris-blue transition-colors">${member.phone}</a>
                            </div>
                            ${member.cell ? `
                            <div class="flex items-center text-zinc-600 text-sm">
                                <i data-lucide="smartphone" class="w-4 h-4 mr-3 text-zinc-400"></i>
                                <a href="tel:${member.cell.replace(/[^0-9]/g, '')}" class="hover:text-morris-blue transition-colors">${member.cell}</a>
                            </div>` : ''}
                        </div>
                    </div>
                </article>
            `).join('');

      return `
                <div class="pt-20">
                    <section class="py-24 bg-zinc-50 relative">
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                            <div class="flex flex-col md:flex-row justify-between items-end mb-16 gap-8">
                                <div class="max-w-2xl">
                                    <h3 class="text-morris-red font-bold text-sm tracking-[0.2em] uppercase mb-4 flex items-center gap-4">
                                        <span class="w-8 h-px bg-morris-red"></span>
                                        Staff Directory
                                    </h3>
                                    <h1 class="text-5xl font-black text-zinc-900 uppercase tracking-tighter mb-6">Our Team</h1>
                                    <p class="text-lg text-zinc-600 leading-relaxed">
                                        Our team is the foundation of everything we do. Each member brings years of experience in export packing, crating, and logistics management, ensuring your cargo receives the ultimate level of care and attention.
                                    </p>
                                </div>
                            </div>

                            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                                ${teamHtml}
                            </div>
                        </div>
                    </section>
                </div>
            `;
    }
'''
if start_team != -1 and end_team != -1:
    content = content[:start_team] + team_new + content[end_team:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
