import sys
import re

file_path = r'c:\Users\suppo\OneDrive\Desktop\Developer\morris-export-\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Contact
start_idx = content.find('function renderContact() {')
end_idx = content.find('function renderCreditApplication() {')

if start_idx != -1 and end_idx != -1:
    contact_new = '''function renderContact() {
      return `
                <div class="pt-20">
                    <section class="relative h-[40vh] flex items-center overflow-hidden">
                        <div class="absolute inset-0 z-0">
                            <img src="images/warehousemanagement/warehousepackaging2.webp" class="w-full h-full object-cover scale-105 animate-[pulse_20s_ease-in-out_infinite]" alt="Contact Background">
                            <div class="absolute inset-0 bg-gradient-to-r from-slate-900/90 to-transparent"></div>
                        </div>
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full pt-10">
                            <h1 class="text-5xl md:text-7xl font-black text-white uppercase tracking-tighter mb-4 drop-shadow-lg">Contact Us</h1>
                            <div class="w-24 h-1.5 bg-morris-red mb-6"></div>
                            <h2 class="text-xl md:text-2xl font-medium text-blue-100 max-w-2xl">We're here to help with your global logistics needs.</h2>
                        </div>
                    </section>

                    <section class="py-24 bg-zinc-50 relative -mt-10 z-20 rounded-t-[3rem] shadow-2xl">
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16">
                                <div>
                                    <h3 class="text-3xl font-black tracking-tight mb-10 uppercase text-zinc-900">Get In Touch</h3>
                                    <div class="space-y-8">
                                        <div class="flex items-start space-x-6 group">
                                            <div class="w-16 h-16 bg-blue-100 text-morris-blue rounded-2xl flex items-center justify-center shrink-0 group-hover:bg-morris-blue group-hover:text-white transition-all shadow-sm">
                                                <i data-lucide="map-pin" class="w-7 h-7"></i>
                                            </div>
                                            <div>
                                                <h4 class="font-bold text-xl mb-2 text-zinc-900">Main Office</h4>
                                                <p class="text-zinc-600 text-lg">8300 Market St<br>Houston, TX 77029</p>
                                            </div>
                                        </div>
                                        <div class="flex items-start space-x-6 group">
                                            <div class="w-16 h-16 bg-red-100 text-morris-red rounded-2xl flex items-center justify-center shrink-0 group-hover:bg-morris-red group-hover:text-white transition-all shadow-sm">
                                                <i data-lucide="phone" class="w-7 h-7"></i>
                                            </div>
                                            <div>
                                                <h4 class="font-bold text-xl mb-2 text-zinc-900">Phone</h4>
                                                <a href="tel:7136721635" class="text-zinc-600 text-lg hover:text-morris-red transition-colors">(713) 672-1635</a>
                                            </div>
                                        </div>
                                        <div class="flex items-start space-x-6 group">
                                            <div class="w-16 h-16 bg-blue-100 text-morris-blue rounded-2xl flex items-center justify-center shrink-0 group-hover:bg-morris-blue group-hover:text-white transition-all shadow-sm">
                                                <i data-lucide="mail" class="w-7 h-7"></i>
                                            </div>
                                            <div>
                                                <h4 class="font-bold text-xl mb-2 text-zinc-900">Email</h4>
                                                <a href="mailto:info@morris-export.com" class="text-zinc-600 text-lg hover:text-morris-blue transition-colors">info@morris-export.com</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="bg-white p-10 md:p-14 rounded-[2rem] border border-zinc-100 shadow-xl">
                                    <h3 class="text-2xl font-black mb-8 uppercase text-zinc-900">Send a Message</h3>
                                    <form class="space-y-6" onsubmit="event.preventDefault(); alert('Message sent! (Simulation)');">
                                        <div class="grid grid-cols-2 gap-6">
                                            <div>
                                                <label class="block text-sm font-bold text-zinc-700 mb-2 uppercase tracking-wide">First Name</label>
                                                <input type="text" required class="w-full px-5 py-4 bg-zinc-50 rounded-xl border border-zinc-200 focus:border-morris-blue focus:ring-2 focus:ring-blue-100 focus:bg-white outline-none transition-all text-lg">
                                            </div>
                                            <div>
                                                <label class="block text-sm font-bold text-zinc-700 mb-2 uppercase tracking-wide">Last Name</label>
                                                <input type="text" required class="w-full px-5 py-4 bg-zinc-50 rounded-xl border border-zinc-200 focus:border-morris-blue focus:ring-2 focus:ring-blue-100 focus:bg-white outline-none transition-all text-lg">
                                            </div>
                                        </div>
                                        <div>
                                            <label class="block text-sm font-bold text-zinc-700 mb-2 uppercase tracking-wide">Email Address</label>
                                            <input type="email" required class="w-full px-5 py-4 bg-zinc-50 rounded-xl border border-zinc-200 focus:border-morris-blue focus:ring-2 focus:ring-blue-100 focus:bg-white outline-none transition-all text-lg">
                                        </div>
                                        <div>
                                            <label class="block text-sm font-bold text-zinc-700 mb-2 uppercase tracking-wide">Message</label>
                                            <textarea rows="4" required class="w-full px-5 py-4 bg-zinc-50 rounded-xl border border-zinc-200 focus:border-morris-blue focus:ring-2 focus:ring-blue-100 focus:bg-white outline-none transition-all text-lg resize-none"></textarea>
                                        </div>
                                        <button type="submit" class="w-full bg-morris-blue text-white font-black uppercase tracking-widest py-5 rounded-xl hover:bg-blue-700 transition-all shadow-lg shadow-blue-900/30">
                                            Send Message
                                        </button>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </section>
                </div>
            `;
    }
'''
    content = content[:start_idx] + contact_new + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated Contact')
