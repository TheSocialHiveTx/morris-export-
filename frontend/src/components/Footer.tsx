import Link from "next/link";
import { MapPin, Phone, Mail, ArrowRight } from "lucide-react";

export default function Footer() {
  return (
    <footer className="bg-zinc-950 text-zinc-400 border-t border-zinc-900 pt-24 pb-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
          {/* Brand */}
          <div className="space-y-6">
            <Link href="/" className="flex items-center gap-3">
              <div className="w-10 h-10 bg-morris-blue flex items-center justify-center rounded-sm">
                <span className="text-white font-black text-xl tracking-tighter">M</span>
              </div>
              <div>
                <span className="text-white font-black text-lg tracking-tight uppercase leading-none block">
                  Morris Export
                </span>
                <span className="text-zinc-500 text-[10px] font-bold tracking-widest uppercase">
                  Services
                </span>
              </div>
            </Link>
            <p className="text-sm leading-relaxed max-w-xs">
              The oldest and largest export packing company on the Gulf Coast. Engineered for global transit since 1942.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="text-white font-black uppercase tracking-widest text-sm mb-6 flex items-center gap-2">
              <span className="w-2 h-2 bg-morris-red block"></span>
              Navigation
            </h4>
            <ul className="space-y-3">
              {['Services', 'Success Stories', 'About & History', 'Customer Hub'].map((item) => (
                <li key={item}>
                  <Link href={`/${item.toLowerCase().replace(/ & /g, '-').replace(/ /g, '-')}`} className="text-sm hover:text-white transition-colors flex items-center gap-2 group">
                    <ArrowRight className="w-3 h-3 text-zinc-600 group-hover:text-morris-blue transition-colors" />
                    {item}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h4 className="text-white font-black uppercase tracking-widest text-sm mb-6 flex items-center gap-2">
              <span className="w-2 h-2 bg-morris-blue block"></span>
              Contact
            </h4>
            <ul className="space-y-4">
              <li className="flex items-start gap-3">
                <MapPin className="w-5 h-5 text-zinc-500 shrink-0 mt-0.5" />
                <span className="text-sm">8300 Market St<br />Houston, TX 77029</span>
              </li>
              <li className="flex items-center gap-3">
                <Phone className="w-5 h-5 text-zinc-500 shrink-0" />
                <a href="tel:7136721635" className="text-sm hover:text-white transition-colors">(713) 672-1635</a>
              </li>
              <li className="flex items-center gap-3">
                <Mail className="w-5 h-5 text-zinc-500 shrink-0" />
                <a href="mailto:info@morris-export.com" className="text-sm hover:text-white transition-colors">info@morris-export.com</a>
              </li>
            </ul>
          </div>

          {/* Accreditations / Certs (Placeholder) */}
          <div>
            <h4 className="text-white font-black uppercase tracking-widest text-sm mb-6 flex items-center gap-2">
              <span className="w-2 h-2 bg-zinc-700 block"></span>
              Accreditations
            </h4>
            <div className="grid grid-cols-2 gap-4">
              <div className="h-16 bg-zinc-900 border border-zinc-800 flex items-center justify-center p-2 grayscale opacity-50 hover:grayscale-0 hover:opacity-100 transition-all">
                <span className="text-[10px] font-bold text-center uppercase">ISO 9001<br/>Certified</span>
              </div>
              <div className="h-16 bg-zinc-900 border border-zinc-800 flex items-center justify-center p-2 grayscale opacity-50 hover:grayscale-0 hover:opacity-100 transition-all">
                <span className="text-[10px] font-bold text-center uppercase">C-TPAT<br/>Compliant</span>
              </div>
            </div>
          </div>
        </div>

        <div className="border-t border-zinc-900 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
          <p className="text-xs font-bold tracking-widest uppercase text-zinc-600">
            &copy; {new Date().getFullYear()} Morris Export Services, Inc.
          </p>
          <div className="flex gap-4">
            <Link href="#" className="text-xs uppercase tracking-widest text-zinc-600 hover:text-white transition-colors">Privacy</Link>
            <Link href="#" className="text-xs uppercase tracking-widest text-zinc-600 hover:text-white transition-colors">Terms</Link>
          </div>
        </div>
      </div>
    </footer>
  );
}
