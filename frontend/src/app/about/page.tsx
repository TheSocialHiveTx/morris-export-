import SectionLayout from "@/components/SectionLayout";
import Image from "next/image";

export default function About() {
  return (
    <>
      <section className="pt-32 pb-16 bg-zinc-950 border-b border-zinc-900 relative overflow-hidden">
        <div className="absolute right-0 top-0 w-1/2 h-full opacity-20">
          <Image src="/images/team/rayvargas.webp" alt="Historical" fill className="object-cover grayscale" />
          <div className="absolute inset-0 bg-gradient-to-r from-zinc-950 to-transparent"></div>
        </div>
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
          <h1 className="text-5xl md:text-7xl font-black text-white uppercase tracking-tighter mb-6">History & <br/>Credentials</h1>
          <p className="text-xl text-zinc-400 max-w-2xl leading-relaxed">
            Since 1942, Morris Export Services has been the backbone of Gulf Coast industrial logistics, blending old-world craftsmanship with modern infrastructure.
          </p>
        </div>
      </section>

      <SectionLayout title="Our Legacy" subtitle="Established 1942">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <div className="space-y-8">
            <p className="text-zinc-400 text-lg leading-relaxed">
              Steeped in history dating back to our establishment in 1942, we have successfully blended old world craftsmanship with today&apos;s modern technology to generate the best service in the packing industry.
            </p>
            <p className="text-zinc-400 text-lg leading-relaxed">
              Morris Export leads industry standards by retaining the most experienced employees in the sector. With over 80 years of operational experience, we&apos;ve gained knowledge and craftsmanship that no other packer can compete with.
            </p>
            <div className="grid grid-cols-2 gap-6 pt-8 border-t border-zinc-800">
              <div>
                <div className="text-4xl font-black text-white mb-2">80+</div>
                <div className="text-xs font-bold text-morris-blue uppercase tracking-widest">Years in Operation</div>
              </div>
              <div>
                <div className="text-4xl font-black text-white mb-2">3rd</div>
                <div className="text-xs font-bold text-morris-blue uppercase tracking-widest">Generation Leadership</div>
              </div>
            </div>
          </div>
          <div className="relative h-[500px] border border-zinc-800 bg-zinc-900 p-2">
            <Image src="/images/team/rayvargas.webp" alt="Team History" fill className="object-cover grayscale hover:grayscale-0 transition-all duration-700" />
            <div className="absolute inset-0 bg-morris-blue mix-blend-multiply opacity-20"></div>
          </div>
        </div>
      </SectionLayout>

      <SectionLayout dark title="Operational Scale" subtitle="Assets & Infrastructure">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-px bg-zinc-800 border border-zinc-800">
          <div className="bg-zinc-900 p-10">
            <h3 className="text-2xl font-black text-white uppercase tracking-tight mb-4">Facilities</h3>
            <ul className="space-y-4 text-zinc-400 text-sm">
              <li className="flex items-center gap-3"><span className="w-1.5 h-1.5 bg-morris-red block"></span> 250,000 Sq Ft Warehouse Space</li>
              <li className="flex items-center gap-3"><span className="w-1.5 h-1.5 bg-morris-red block"></span> 20 Acres Paved Concrete Staging</li>
              <li className="flex items-center gap-3"><span className="w-1.5 h-1.5 bg-morris-red block"></span> Climate Controlled Zones</li>
            </ul>
          </div>
          <div className="bg-zinc-900 p-10">
            <h3 className="text-2xl font-black text-white uppercase tracking-tight mb-4">Lifting</h3>
            <ul className="space-y-4 text-zinc-400 text-sm">
              <li className="flex items-center gap-3"><span className="w-1.5 h-1.5 bg-morris-blue block"></span> 140,000 lbs Max Forklift Capacity</li>
              <li className="flex items-center gap-3"><span className="w-1.5 h-1.5 bg-morris-blue block"></span> Overhead Crane Systems</li>
              <li className="flex items-center gap-3"><span className="w-1.5 h-1.5 bg-morris-blue block"></span> Specialized Rigging Teams</li>
            </ul>
          </div>
          <div className="bg-zinc-900 p-10">
            <h3 className="text-2xl font-black text-white uppercase tracking-tight mb-4">Transport</h3>
            <ul className="space-y-4 text-zinc-400 text-sm">
              <li className="flex items-center gap-3"><span className="w-1.5 h-1.5 bg-zinc-500 block"></span> Private Heavy Haul Fleet</li>
              <li className="flex items-center gap-3"><span className="w-1.5 h-1.5 bg-zinc-500 block"></span> Escort & Permitting Services</li>
              <li className="flex items-center gap-3"><span className="w-1.5 h-1.5 bg-zinc-500 block"></span> Port Drayage Operations</li>
            </ul>
          </div>
        </div>
      </SectionLayout>
    </>
  );
}
