import sys

file_path = r'c:\Users\suppo\OneDrive\Desktop\Developer\morris-export-\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Update Body
text = text.replace('<body class="antialiased text-zinc-900 bg-white">', '<body class="antialiased text-zinc-300 bg-zinc-950">')

# Update Nav
start_nav = text.find('<!-- Navbar -->')
end_nav = text.find('</nav>') + 6

new_nav = '''<!-- Navbar -->
  <nav class="fixed w-full z-50 bg-zinc-950/90 backdrop-blur-xl border-b border-white/10 shadow-2xl transition-all duration-300 modern-nav">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-24 items-center">
        <!-- Logo -->
        <a href="#/" class="flex-shrink-0 flex items-center group gap-4">
          <div class="w-12 h-12 bg-morris-blue flex items-center justify-center rounded-sm shadow-[0_0_15px_rgba(37,99,235,0.5)]">
            <span class="text-white font-black text-2xl tracking-tighter">M</span>
          </div>
          <div class="flex flex-col justify-center">
            <span class="text-white font-black text-xl tracking-tight uppercase leading-none group-hover:text-morris-blue transition-colors">Morris Export</span>
            <span class="text-zinc-500 text-xs font-bold tracking-widest uppercase">Services</span>
          </div>
        </a>
        <div class="hidden lg:flex items-center space-x-10" id="nav-links">
          <!-- Links injected via JS, but we'll style them dark -->
        </div>

        <div class="lg:hidden flex items-center absolute right-4">
          <button id="mobile-menu-button" class="text-zinc-400 hover:text-white transition-colors">
            <i data-lucide="menu" class="w-8 h-8"></i>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile menu -->
    <div id="mobile-menu" class="hidden lg:hidden bg-zinc-950 border-b border-zinc-800 shadow-2xl">
      <div class="px-4 py-6 border-b border-zinc-900 mb-2 flex items-center gap-4">
        <div class="w-10 h-10 bg-morris-blue flex items-center justify-center rounded-sm">
            <span class="text-white font-black text-xl tracking-tighter">M</span>
        </div>
        <span class="text-white font-black text-lg tracking-tight uppercase">Morris Export</span>
      </div>
      <div class="px-4 pt-2 pb-8 space-y-2" id="mobile-nav-links">
        <!-- Links injected via JS -->
      </div>
    </div>
  </nav>'''

if start_nav != -1 and end_nav != -1:
    text = text[:start_nav] + new_nav + text[end_nav:]

# Update Footer
start_foot = text.find('<!-- Footer -->')
end_foot = text.find('</footer>') + 9

new_foot = '''<!-- Footer -->
  <footer class="bg-zinc-950 text-zinc-400 py-20 border-t border-zinc-900 relative overflow-hidden mt-20">
    <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-morris-blue/5 via-zinc-950 to-zinc-950"></div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-16">
        <div class="col-span-1 md:col-span-2">
          <a href="#/" class="mb-8 flex items-center gap-4 group">
            <div class="w-12 h-12 bg-morris-blue flex items-center justify-center rounded-sm">
                <span class="text-white font-black text-2xl tracking-tighter">M</span>
            </div>
            <div class="flex flex-col justify-center">
                <span class="text-white font-black text-xl tracking-tight uppercase leading-none group-hover:text-morris-blue transition-colors">Morris Export</span>
                <span class="text-zinc-500 text-xs font-bold tracking-widest uppercase">Services</span>
            </div>
          </a>
          <p class="max-w-md mb-8 text-zinc-500 text-lg leading-relaxed">
            Providing world-class export packing, crating, and logistics solutions since 1942.
            Your partner in global industrial transportation.
          </p>
          <div class="flex space-x-6">
            <a href="tel:7136721635" class="flex items-center space-x-3 text-zinc-400 hover:text-morris-blue transition-colors group">
              <div class="w-10 h-10 bg-zinc-900 rounded-full flex items-center justify-center group-hover:bg-blue-900/30">
                <i data-lucide="phone" class="w-4 h-4"></i>
              </div>
              <span class="font-medium">(713) 672-1635</span>
            </a>
          </div>
        </div>

        <div>
          <h4 class="text-white font-black uppercase tracking-widest mb-8 text-sm">Quick Links</h4>
          <ul class="space-y-4">
            <li><a href="#/about-us" class="hover:text-morris-blue transition-colors flex items-center gap-2"><i data-lucide="chevron-right" class="w-3 h-3 text-morris-blue"></i> About Us</a></li>
            <li><a href="#/services" class="hover:text-morris-blue transition-colors flex items-center gap-2"><i data-lucide="chevron-right" class="w-3 h-3 text-morris-blue"></i> Services</a></li>
            <li><a href="#/facilities" class="hover:text-morris-blue transition-colors flex items-center gap-2"><i data-lucide="chevron-right" class="w-3 h-3 text-morris-blue"></i> Facilities</a></li>
            <li><a href="#/contact-us" class="hover:text-morris-blue transition-colors flex items-center gap-2"><i data-lucide="chevron-right" class="w-3 h-3 text-morris-blue"></i> Contact</a></li>
          </ul>
        </div>

        <div>
          <h4 class="text-white font-black uppercase tracking-widest mb-8 text-sm">Legal</h4>
          <ul class="space-y-4">
            <li><a href="#/terms-and-conditions" class="hover:text-morris-blue transition-colors flex items-center gap-2"><i data-lucide="chevron-right" class="w-3 h-3 text-morris-blue"></i> Terms & Conditions</a></li>
            <li><a href="#/html-sitemap" class="hover:text-morris-blue transition-colors flex items-center gap-2"><i data-lucide="chevron-right" class="w-3 h-3 text-morris-blue"></i> Sitemap</a></li>
          </ul>
        </div>
      </div>

      <div class="mt-20 pt-8 border-t border-zinc-900 text-sm flex flex-col md:flex-row justify-between items-center text-zinc-600">
        <p> <span id="current-year"></span> Morris Export Services. All rights reserved.</p>
        <p class="mt-4 md:mt-0 font-bold tracking-widest uppercase text-xs">Houston, Texas</p>
      </div>
    </div>
  </footer>'''

if start_foot != -1 and end_foot != -1:
    text = text[:start_foot] + new_foot + text[end_foot:]

# Update the updateNavActiveStates function
text = text.replace('text-zinc-600 hover:text-blue-600', 'text-zinc-400 hover:text-white font-bold uppercase tracking-widest text-sm')
text = text.replace('text-blue-600 font-bold', 'text-white font-black uppercase tracking-widest text-sm border-b-2 border-morris-blue pb-1')

# For mobile links:
text = text.replace('block px-4 py-3 rounded-xl text-base font-medium transition-colors', 'block px-4 py-4 border-b border-zinc-900 text-sm font-bold uppercase tracking-widest transition-colors')
text = text.replace("cls = isActive ? 'bg-blue-50 text-blue-600 font-bold' : 'text-zinc-700 hover:bg-zinc-50 hover:text-blue-600';", "cls = isActive ? 'text-white bg-zinc-900' : 'text-zinc-500 hover:bg-zinc-900 hover:text-white';")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated nav and footer in index.html")
