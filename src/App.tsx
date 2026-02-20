/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { BrowserRouter as Router, Routes, Route, Link, useLocation } from 'react-router-dom';
import { motion, AnimatePresence } from 'motion/react';
import { Menu, X, Phone, Mail, MapPin, ChevronRight, ExternalLink } from 'lucide-react';
import { useState, useEffect } from 'react';
import { SERVICES } from './constants';

// Components
const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const location = useLocation();

  const navLinks = [
    { name: 'Home', path: '/' },
    { name: 'About', path: '/about-us' },
    { name: 'Services', path: '/services' },
    { name: 'Facilities', path: '/facilities' },
    { name: 'Customer Center', path: '/customer-center' },
    { name: 'Contact', path: '/contact-us' },
  ];

  return (
    <nav className="fixed w-full z-50 bg-white/90 backdrop-blur-md border-b border-zinc-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-20">
          <div className="flex items-center">
            <Link to="/" className="flex-shrink-0 flex items-center">
              <span className="text-2xl font-black tracking-tighter text-zinc-900">MORRIS<span className="text-blue-600">EXPORT</span></span>
            </Link>
          </div>
          
          <div className="hidden md:flex items-center space-x-8">
            {navLinks.map((link) => (
              <Link
                key={link.path}
                to={link.path}
                className={`text-sm font-medium transition-colors hover:text-blue-600 ${
                  location.pathname === link.path ? 'text-blue-600' : 'text-zinc-600'
                }`}
              >
                {link.name}
              </Link>
            ))}
          </div>

          <div className="md:hidden flex items-center">
            <button
              onClick={() => setIsOpen(!isOpen)}
              className="text-zinc-600 hover:text-zinc-900"
            >
              {isOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile menu */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            className="md:hidden bg-white border-b border-zinc-200 overflow-hidden"
          >
            <div className="px-4 pt-2 pb-6 space-y-1">
              {navLinks.map((link) => (
                <Link
                  key={link.path}
                  to={link.path}
                  onClick={() => setIsOpen(false)}
                  className="block px-3 py-4 text-base font-medium text-zinc-600 hover:text-blue-600 hover:bg-zinc-50 rounded-lg"
                >
                  {link.name}
                </Link>
              ))}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </nav>
  );
};

const Footer = () => (
  <footer className="bg-zinc-900 text-zinc-400 py-16">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="grid grid-cols-1 md:grid-cols-4 gap-12">
        <div className="col-span-1 md:col-span-2">
          <span className="text-2xl font-black tracking-tighter text-white mb-6 block">MORRIS<span className="text-blue-500">EXPORT</span></span>
          <p className="max-w-md mb-8">
            Providing world-class export packing, crating, and logistics solutions since 1958. 
            Your partner in global industrial transportation.
          </p>
          <div className="flex space-x-4">
            <div className="flex items-center space-x-2">
              <Phone size={18} />
              <span>(713) 672-1635</span>
            </div>
          </div>
        </div>
        
        <div>
          <h4 className="text-white font-bold mb-6">Quick Links</h4>
          <ul className="space-y-4">
            <li><Link to="/about-us" className="hover:text-white transition-colors">About Us</Link></li>
            <li><Link to="/services" className="hover:text-white transition-colors">Services</Link></li>
            <li><Link to="/facilities" className="hover:text-white transition-colors">Facilities</Link></li>
            <li><Link to="/contact-us" className="hover:text-white transition-colors">Contact</Link></li>
          </ul>
        </div>

        <div>
          <h4 className="text-white font-bold mb-6">Legal</h4>
          <ul className="space-y-4">
            <li><Link to="/terms-and-conditions" className="hover:text-white transition-colors">Terms & Conditions</Link></li>
            <li><Link to="/html-sitemap" className="hover:text-white transition-colors">Sitemap</Link></li>
          </ul>
        </div>
      </div>
      
      <div className="mt-16 pt-8 border-t border-zinc-800 text-sm flex flex-col md:flex-row justify-between items-center">
        <p>© {new Date().getFullYear()} Morris Export Services. All rights reserved.</p>
        <p className="mt-4 md:mt-0">Houston, Texas</p>
      </div>
    </div>
  </footer>
);

// Page Components
const Home = () => (
  <div className="pt-20">
    <section className="relative h-[80vh] flex items-center overflow-hidden bg-zinc-900">
      <div className="absolute inset-0 opacity-40">
        <img 
          src="https://picsum.photos/seed/industrial/1920/1080" 
          alt="Industrial Port" 
          className="w-full h-full object-cover"
          referrerPolicy="no-referrer"
        />
      </div>
      <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-white">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          <h1 className="text-5xl md:text-7xl font-black tracking-tight mb-6">
            ENGINEERED FOR <br />
            <span className="text-blue-500">GLOBAL TRANSIT</span>
          </h1>
          <p className="text-xl text-zinc-300 max-w-2xl mb-10">
            Export packing, crating, and logistics solutions for the world's most demanding industrial projects.
          </p>
          <div className="flex flex-col sm:flex-row gap-4">
            <Link to="/services" className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-lg font-bold text-center transition-all">
              Our Services
            </Link>
            <Link to="/contact-us" className="bg-white/10 hover:bg-white/20 backdrop-blur-md text-white px-8 py-4 rounded-lg font-bold text-center border border-white/30 transition-all">
              Get a Quote
            </Link>
          </div>
        </motion.div>
      </div>
    </section>

    <section className="py-24 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-12">
          <div className="p-8 bg-zinc-50 rounded-2xl border border-zinc-100">
            <h3 className="text-2xl font-bold mb-4">65+ Years</h3>
            <p className="text-zinc-600">Decades of experience handling complex industrial logistics and export requirements.</p>
          </div>
          <div className="p-8 bg-zinc-50 rounded-2xl border border-zinc-100">
            <h3 className="text-2xl font-bold mb-4">Strategic Location</h3>
            <p className="text-zinc-600">Based in Houston, Texas, with direct access to one of the world's busiest ports.</p>
          </div>
          <div className="p-8 bg-zinc-50 rounded-2xl border border-zinc-100">
            <h3 className="text-2xl font-bold mb-4">M-Pact Technology</h3>
            <p className="text-zinc-600">Proprietary software providing real-time visibility into your cargo and inventory.</p>
          </div>
        </div>
      </div>
    </section>
  </div>
);

const ServicesHub = () => (
  <div className="pt-32 pb-24 bg-zinc-50">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="mb-16">
        <h1 className="text-4xl font-black tracking-tight mb-4">OUR SERVICES</h1>
        <p className="text-xl text-zinc-600 max-w-3xl">
          Comprehensive industrial packing and logistics solutions tailored to your specific project needs.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {SERVICES.map((service) => (
          <Link 
            key={service.id} 
            to={`/services/${service.slug}`}
            className="group bg-white p-8 rounded-2xl border border-zinc-200 hover:border-blue-500 transition-all shadow-sm hover:shadow-md"
          >
            <div className="w-12 h-12 bg-blue-50 text-blue-600 rounded-xl flex items-center justify-center mb-6 group-hover:bg-blue-600 group-hover:text-white transition-colors">
              <service.icon size={24} />
            </div>
            <h3 className="text-xl font-bold mb-3">{service.title}</h3>
            <p className="text-zinc-600 mb-6">{service.description}</p>
            <div className="flex items-center text-blue-600 font-bold text-sm">
              Learn More <ChevronRight size={16} className="ml-1" />
            </div>
          </Link>
        ))}
      </div>
    </div>
  </div>
);

const ServiceDetail = () => {
  const location = useLocation();
  const slug = location.pathname.split('/').pop();
  const service = SERVICES.find(s => s.slug === slug);

  if (!service) return <div className="pt-32 text-center">Service not found</div>;

  return (
    <div className="pt-32 pb-24">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <Link to="/services" className="text-blue-600 font-medium mb-8 inline-flex items-center hover:underline">
          <ChevronRight size={16} className="mr-1 rotate-180" /> Back to Services
        </Link>
        <div className="flex items-center space-x-4 mb-8">
          <div className="w-16 h-16 bg-blue-600 text-white rounded-2xl flex items-center justify-center">
            <service.icon size={32} />
          </div>
          <h1 className="text-4xl font-black tracking-tight">{service.title}</h1>
        </div>
        <div className="prose prose-zinc lg:prose-xl max-w-none">
          <p className="text-xl text-zinc-600 leading-relaxed mb-8">
            {service.content}
          </p>
          <div className="bg-zinc-50 p-8 rounded-2xl border border-zinc-200 mb-12">
            <h3 className="text-xl font-bold mb-4">Key Features</h3>
            <ul className="space-y-3 text-zinc-600">
              <li className="flex items-start"><ChevronRight size={18} className="mr-2 text-blue-600 mt-1" /> Engineered for maximum protection</li>
              <li className="flex items-start"><ChevronRight size={18} className="mr-2 text-blue-600 mt-1" /> Compliant with international export standards</li>
              <li className="flex items-start"><ChevronRight size={18} className="mr-2 text-blue-600 mt-1" /> Tailored to specific cargo requirements</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

const About = () => (
  <div className="pt-32 pb-24">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
        <div>
          <h1 className="text-4xl font-black tracking-tight mb-8">ABOUT MORRIS EXPORT</h1>
          <p className="text-lg text-zinc-600 mb-6 leading-relaxed">
            Founded in 1958, Morris Export Services has grown from a small family operation into a leading provider of industrial export packing and logistics. 
            Our commitment to quality, safety, and innovation has made us the preferred partner for global energy, manufacturing, and construction firms.
          </p>
          <p className="text-lg text-zinc-600 mb-8 leading-relaxed">
            We operate from strategic facilities in Houston, providing our clients with the expertise and infrastructure needed to move their most critical assets anywhere in the world.
          </p>
          <div className="grid grid-cols-2 gap-8">
            <div>
              <div className="text-3xl font-black text-blue-600 mb-2">1958</div>
              <div className="text-sm font-bold text-zinc-500 uppercase tracking-widest">Established</div>
            </div>
            <div>
              <div className="text-3xl font-black text-blue-600 mb-2">Houston</div>
              <div className="text-sm font-bold text-zinc-500 uppercase tracking-widest">Headquarters</div>
            </div>
          </div>
        </div>
        <div className="rounded-3xl overflow-hidden shadow-2xl">
          <img 
            src="https://picsum.photos/seed/warehouse/800/1000" 
            alt="Warehouse Operations" 
            className="w-full h-full object-cover"
            referrerPolicy="no-referrer"
          />
        </div>
      </div>
    </div>
  </div>
);

const Facilities = () => (
  <div className="pt-32 pb-24 bg-zinc-50">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 className="text-4xl font-black tracking-tight mb-12">OUR FACILITIES</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-12">
        <div className="bg-white p-10 rounded-3xl border border-zinc-200 shadow-sm">
          <Warehouse className="text-blue-600 mb-6" size={48} />
          <h2 className="text-2xl font-bold mb-4">Strategic Storage & Warehousing</h2>
          <p className="text-zinc-600 mb-6">
            Our facilities offer over 250,000 square feet of indoor storage and extensive outdoor laydown areas, all secured and monitored 24/7.
          </p>
          <ul className="space-y-3 text-zinc-600">
            <li className="flex items-center"><ChevronRight size={16} className="mr-2 text-blue-600" /> Climate-controlled options</li>
            <li className="flex items-center"><ChevronRight size={16} className="mr-2 text-blue-600" /> Heavy-lift capabilities</li>
            <li className="flex items-center"><ChevronRight size={16} className="mr-2 text-blue-600" /> Inventory management via M-Pact</li>
          </ul>
        </div>
        <div className="rounded-3xl overflow-hidden">
          <img 
            src="https://picsum.photos/seed/facility/800/600" 
            alt="Facility Overview" 
            className="w-full h-full object-cover"
            referrerPolicy="no-referrer"
          />
        </div>
      </div>
    </div>
  </div>
);

const CustomerCenter = () => (
  <div className="pt-32 pb-24">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 className="text-4xl font-black tracking-tight mb-12">CUSTOMER CENTER</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        <a 
          href="https://webstars.morris-export.com" 
          target="_blank" 
          rel="noopener noreferrer"
          className="p-8 bg-blue-600 text-white rounded-2xl hover:bg-blue-700 transition-all flex flex-col justify-between"
        >
          <div>
            <ExternalLink size={32} className="mb-6 opacity-50" />
            <h3 className="text-2xl font-bold mb-4">Customer Reports</h3>
            <p className="opacity-80">Access your real-time tracking and inventory reports via our Webstars portal.</p>
          </div>
          <div className="mt-8 font-bold flex items-center">
            Login Now <ChevronRight size={16} className="ml-1" />
          </div>
        </a>
        
        <Link to="/credit-application" className="p-8 bg-zinc-100 text-zinc-900 rounded-2xl hover:bg-zinc-200 transition-all flex flex-col justify-between border border-zinc-200">
          <div>
            <ClipboardList size={32} className="mb-6 text-zinc-400" />
            <h3 className="text-2xl font-bold mb-4">Credit Application</h3>
            <p className="text-zinc-600">Download and submit our credit application to establish an account with us.</p>
          </div>
          <div className="mt-8 font-bold text-blue-600 flex items-center">
            View Application <ChevronRight size={16} className="ml-1" />
          </div>
        </Link>

        <Link to="/faq" className="p-8 bg-zinc-100 text-zinc-900 rounded-2xl hover:bg-zinc-200 transition-all flex flex-col justify-between border border-zinc-200">
          <div>
            <Phone size={32} className="mb-6 text-zinc-400" />
            <h3 className="text-2xl font-bold mb-4">FAQ</h3>
            <p className="text-zinc-600">Find answers to common questions about our services and procedures.</p>
          </div>
          <div className="mt-8 font-bold text-blue-600 flex items-center">
            Read FAQs <ChevronRight size={16} className="ml-1" />
          </div>
        </Link>
      </div>
    </div>
  </div>
);

const Contact = () => (
  <div className="pt-32 pb-24">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-16">
        <div>
          <h1 className="text-4xl font-black tracking-tight mb-8">CONTACT US</h1>
          <div className="space-y-8">
            <div className="flex items-start space-x-4">
              <div className="w-12 h-12 bg-blue-50 text-blue-600 rounded-xl flex items-center justify-center flex-shrink-0">
                <MapPin size={24} />
              </div>
              <div>
                <h3 className="font-bold text-lg mb-1">Main Office</h3>
                <p className="text-zinc-600">8300 Market St, Houston, TX 77029</p>
              </div>
            </div>
            <div className="flex items-start space-x-4">
              <div className="w-12 h-12 bg-blue-50 text-blue-600 rounded-xl flex items-center justify-center flex-shrink-0">
                <Phone size={24} />
              </div>
              <div>
                <h3 className="font-bold text-lg mb-1">Phone</h3>
                <p className="text-zinc-600">(713) 672-1635</p>
              </div>
            </div>
            <div className="flex items-start space-x-4">
              <div className="w-12 h-12 bg-blue-50 text-blue-600 rounded-xl flex items-center justify-center flex-shrink-0">
                <Mail size={24} />
              </div>
              <div>
                <h3 className="font-bold text-lg mb-1">Email</h3>
                <p className="text-zinc-600">info@morris-export.com</p>
              </div>
            </div>
          </div>
        </div>
        
        <div className="bg-zinc-50 p-10 rounded-3xl border border-zinc-200">
          <h3 className="text-2xl font-bold mb-6">Send a Message</h3>
          <form className="space-y-4">
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-bold text-zinc-700 mb-2">First Name</label>
                <input type="text" className="w-full px-4 py-3 rounded-xl border border-zinc-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none transition-all" />
              </div>
              <div>
                <label className="block text-sm font-bold text-zinc-700 mb-2">Last Name</label>
                <input type="text" className="w-full px-4 py-3 rounded-xl border border-zinc-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none transition-all" />
              </div>
            </div>
            <div>
              <label className="block text-sm font-bold text-zinc-700 mb-2">Email Address</label>
              <input type="email" className="w-full px-4 py-3 rounded-xl border border-zinc-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none transition-all" />
            </div>
            <div>
              <label className="block text-sm font-bold text-zinc-700 mb-2">Message</label>
              <textarea rows={4} className="w-full px-4 py-3 rounded-xl border border-zinc-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none transition-all"></textarea>
            </div>
            <button className="w-full bg-blue-600 text-white font-bold py-4 rounded-xl hover:bg-blue-700 transition-all">
              Send Message
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
);

const Terms = () => (
  <div className="pt-32 pb-24">
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 className="text-4xl font-black tracking-tight mb-8">TERMS AND CONDITIONS</h1>
      <div className="prose prose-zinc lg:prose-lg max-w-none">
        <p className="mb-8">
          All services provided by Morris Export Services are subject to our standard terms and conditions. 
          Please review the full document for detailed information regarding liabilities, responsibilities, and service agreements.
        </p>
        <a 
          href="/wp-content/uploads/2019/06/Terms-And-Conditions.pdf" 
          className="inline-flex items-center bg-zinc-900 text-white px-8 py-4 rounded-xl font-bold hover:bg-zinc-800 transition-all"
        >
          Download Full Terms (PDF) <ExternalLink size={18} className="ml-2" />
        </a>
      </div>
    </div>
  </div>
);

const OurTeam = () => (
  <div className="pt-32 pb-24">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 className="text-4xl font-black tracking-tight mb-12">OUR TEAM</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-12">
        {[1, 2, 3].map((i) => (
          <div key={i} className="group">
            <div className="aspect-square rounded-3xl overflow-hidden mb-6 bg-zinc-100">
              <img 
                src={`https://picsum.photos/seed/team${i}/600/600`} 
                alt="Team Member" 
                className="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-500"
                referrerPolicy="no-referrer"
              />
            </div>
            <h3 className="text-xl font-bold">Team Member {i}</h3>
            <p className="text-zinc-500">Department Lead</p>
          </div>
        ))}
      </div>
    </div>
  </div>
);

const FAQ = () => (
  <div className="pt-32 pb-24">
    <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 className="text-4xl font-black tracking-tight mb-12">FREQUENTLY ASKED QUESTIONS</h1>
      <div className="space-y-6">
        {[
          { q: "What are your standard operating hours?", a: "We are open Monday through Friday, 7:00 AM to 5:00 PM CST. Special arrangements can be made for after-hours or weekend requirements." },
          { q: "Do you provide on-site services?", a: "Yes, our mobile packing teams can provide full crating and securing services at your facility." },
          { q: "Are you certified for hazardous materials?", a: "Yes, we are fully certified to handle, package, and document hazardous materials for international export." }
        ].map((item, i) => (
          <div key={i} className="p-8 bg-zinc-50 rounded-2xl border border-zinc-200">
            <h3 className="text-xl font-bold mb-3">{item.q}</h3>
            <p className="text-zinc-600">{item.a}</p>
          </div>
        ))}
      </div>
    </div>
  </div>
);

export default function App() {
  return (
    <Router>
      <div className="min-h-screen bg-white font-sans text-zinc-900 selection:bg-blue-100 selection:text-blue-900">
        <Navbar />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about-us" element={<About />} />
            <Route path="/services" element={<ServicesHub />} />
            <Route path="/services/:slug" element={<ServiceDetail />} />
            <Route path="/facilities" element={<Facilities />} />
            <Route path="/customer-center" element={<CustomerCenter />} />
            <Route path="/contact-us" element={<Contact />} />
            <Route path="/credit-application" element={<div>Credit Application Page Content</div>} />
            <Route path="/faq" element={<FAQ />} />
            <Route path="/our-team" element={<OurTeam />} />
            <Route path="/terms-and-conditions" element={<Terms />} />
            <Route path="/html-sitemap" element={<div>HTML Sitemap Content</div>} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}
