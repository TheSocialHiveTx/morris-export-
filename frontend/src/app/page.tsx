import Image from "next/image";
import Link from "next/link";
import SectionLayout from "@/components/SectionLayout";
import ServiceCard from "@/components/ServiceCard";
import { ShieldCheck, Anchor, Truck, Warehouse, CheckCircle2, ArrowRight } from "lucide-react";

export default function Home() {
  return (
    <>
      {/* Hero Section */}
      <section className="relative min-h-[90vh] flex items-center pt-24 pb-16 overflow-hidden">
        <div className="absolute inset-0 z-0">
          <Image
            src="/images/warehousemanagement/warehousepackaging2.webp"
            alt="Industrial Logistics"
            fill
            className="object-cover object-center grayscale-[0.2]"
            priority
          />
          <div className="absolute inset-0 bg-gradient-to-r from-zinc-950 via-zinc-950/80 to-transparent"></div>
        </div>

        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full">
          <div className="max-w-3xl">
            <div className="inline-flex items-center gap-2 px-3 py-1 bg-zinc-900 border border-zinc-700 mb-8">
              <span className="w-2 h-2 rounded-full bg-morris-red animate-pulse"></span>
              <span className="text-xs font-bold text-zinc-300 uppercase tracking-widest">Active Operations</span>
            </div>
            
            <h1 className="text-6xl md:text-8xl font-black text-white uppercase tracking-tighter leading-[0.9] mb-8">
              Engineered <br/>
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-zinc-400 to-zinc-600">For Global</span> <br/>
              Transit
            </h1>
            
            <p className="text-lg md:text-xl text-zinc-400 max-w-2xl leading-relaxed mb-10 font-medium">
              The largest and oldest export packer on the Gulf Coast. Asset-based logistics, specialized crating, and heavy-haul operations built for the world&apos;s toughest industrial challenges.
            </p>
            
            <div className="flex flex-col sm:flex-row gap-4">
              <Link href="/contact" className="bg-morris-red hover:bg-red-700 text-white px-8 py-4 font-black uppercase tracking-widest text-center transition-all flex items-center justify-center gap-2 group">
                Start Your Project
              </Link>
              <Link href="/services" className="bg-zinc-900 border border-zinc-700 hover:bg-zinc-800 text-white px-8 py-4 font-black uppercase tracking-widest text-center transition-all flex items-center justify-center gap-2">
                Explore Capabilities
              </Link>
            </div>
          </div>
        </div>

        {/* Floating Stats */}
        <div className="hidden lg:block absolute bottom-12 right-12 z-20">
          <div className="grid grid-cols-2 gap-px bg-zinc-800 border border-zinc-800 shadow-2xl">
            <div className="bg-zinc-950 p-6 w-48">
              <div className="text-4xl font-black text-white mb-1">80+</div>
              <div className="text-[10px] text-zinc-500 font-bold uppercase tracking-widest">Years Experience</div>
            </div>
            <div className="bg-zinc-950 p-6 w-48">
              <div className="text-4xl font-black text-white mb-1">250K</div>
              <div className="text-[10px] text-zinc-500 font-bold uppercase tracking-widest">Sq Ft Facilities</div>
            </div>
            <div className="bg-zinc-950 p-6 w-48">
              <div className="text-4xl font-black text-white mb-1">140K</div>
              <div className="text-[10px] text-zinc-500 font-bold uppercase tracking-widest">Lbs Lift Capacity</div>
            </div>
            <div className="bg-zinc-950 p-6 w-48">
              <div className="text-4xl font-black text-white mb-1">24/7</div>
              <div className="text-[10px] text-zinc-500 font-bold uppercase tracking-widest">Operational Support</div>
            </div>
          </div>
        </div>
      </section>

      {/* Why Choose Us */}
      <SectionLayout dark title="Infrastructure & Capacity" subtitle="Why Choose Us">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {[
            { icon: <ShieldCheck className="w-8 h-8"/>, title: "Asset-Based", desc: "We own our facilities, fleets, and equipment for total control." },
            { icon: <Anchor className="w-8 h-8"/>, title: "Port Proximate", desc: "Strategic locations near major Gulf Coast shipping channels." },
            { icon: <Warehouse className="w-8 h-8"/>, title: "Bonded Storage", desc: "Secure, climate-controlled, and foreign trade zone capabilities." },
            { icon: <Truck className="w-8 h-8"/>, title: "Heavy Haul Fleet", desc: "Private fleet capable of transporting extreme dimensions." }
          ].map((item, i) => (
            <div key={i} className="p-8 bg-zinc-900 border border-zinc-800 hover:border-zinc-700 transition-colors">
              <div className="w-16 h-16 bg-zinc-950 flex items-center justify-center text-morris-blue mb-6">
                {item.icon}
              </div>
              <h3 className="text-xl font-black text-white uppercase tracking-tight mb-3">{item.title}</h3>
              <p className="text-zinc-400 text-sm leading-relaxed">{item.desc}</p>
            </div>
          ))}
        </div>
      </SectionLayout>

      {/* Services Overview */}
      <SectionLayout title="Core Operations" subtitle="Our Services">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <ServiceCard 
            title="Export Packing & Crating"
            description="Custom engineered wooden crates, vapor barrier packaging, and ISPM-15 certified materials for global compliance."
            image="/images/crating/customcrating.webp"
            link="/services#crating"
          />
          <ServiceCard 
            title="Heavy Assets & Breakbulk"
            description="Specialized lifting, securing, and transloading of oversized industrial machinery and energy infrastructure."
            image="/images/crane/img1-1.jpg.webp"
            link="/services#heavy"
          />
          <ServiceCard 
            title="Warehousing & Storage"
            description="Short and long-term secure storage, inventory management, and staging for complex project cargo."
            image="/images/facilitiesstorage/Secure Facilities.webp"
            link="/services#warehousing"
          />
        </div>
        <div className="mt-12 text-center">
          <Link href="/services" className="inline-flex items-center text-sm font-bold uppercase tracking-widest text-white hover:text-morris-blue transition-colors">
            View All Capabilities <ArrowRight className="ml-2 w-4 h-4" />
          </Link>
        </div>
      </SectionLayout>

      {/* Success Stories Preview */}
      <SectionLayout dark>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <div>
            <h3 className="text-morris-red font-bold text-sm tracking-[0.2em] uppercase mb-4 flex items-center gap-4">
              <span className="w-8 h-px bg-morris-red"></span>
              Success Stories
            </h3>
            <h2 className="text-4xl md:text-5xl font-black uppercase tracking-tighter text-white mb-8">
              Proven <br/> Performance
            </h2>
            <p className="text-zinc-400 text-lg leading-relaxed mb-8">
              From relocating entire manufacturing facilities to shipping delicate aerospace components, our track record speaks for itself. We engineer solutions for the most complex logistical challenges.
            </p>
            <ul className="space-y-4 mb-10">
              {['Energy & Petrochemical', 'Aerospace & Defense', 'Manufacturing', 'Construction'].map(industry => (
                <li key={industry} className="flex items-center gap-3">
                  <CheckCircle2 className="w-5 h-5 text-morris-blue" />
                  <span className="text-zinc-300 font-bold uppercase tracking-wider text-sm">{industry}</span>
                </li>
              ))}
            </ul>
            <Link href="/success-stories" className="bg-white text-zinc-950 px-8 py-4 font-black uppercase tracking-widest inline-block hover:bg-zinc-200 transition-colors">
              Read Case Studies
            </Link>
          </div>
          <div className="relative h-[600px] border border-zinc-800">
            <Image 
              src="/images/containerization/container1.webp"
              alt="Project Cargo"
              fill
              className="object-cover grayscale hover:grayscale-0 transition-all duration-700"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-zinc-950 to-transparent opacity-80"></div>
            <div className="absolute bottom-10 left-10 right-10">
              <div className="bg-zinc-950/90 backdrop-blur-md p-6 border border-zinc-800">
                <h4 className="text-white font-black uppercase tracking-tight text-xl mb-2">Project: Delta Refinery</h4>
                <p className="text-zinc-400 text-sm">Transloaded and secured 40+ oversized units for maritime transport.</p>
              </div>
            </div>
          </div>
        </div>
      </SectionLayout>
    </>
  );
}
