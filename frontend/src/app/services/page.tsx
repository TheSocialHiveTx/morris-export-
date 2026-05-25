import SectionLayout from "@/components/SectionLayout";
import ServiceCard from "@/components/ServiceCard";
import Image from "next/image";

export default function Services() {
  const categories = [
    {
      title: "Packing & Crating",
      description: "Industrial strength export packing.",
      services: [
        { title: "Custom Wooden Crating", desc: "Engineered specs for any dimension.", img: "/images/crating/customcrating.webp" },
        { title: "Vapor Barrier & Shrinkwrap", desc: "Protection against moisture and salt.", img: "/images/vinyl wrap protection/vinylwrap2.webp" },
        { title: "Onsite Packing", desc: "We deploy our crews to your facility.", img: "/images/onsitepacking/onsitepacking3.webp" }
      ]
    },
    {
      title: "Logistics & Operations",
      description: "Movement of massive assets.",
      services: [
        { title: "Containerization", desc: "Flat racks, open tops, and standard boxes.", img: "/images/containerization/container1.webp" },
        { title: "Heavy Lift & Transloading", desc: "140K lbs lift capacity on site.", img: "/images/crane/crane.webp" },
        { title: "Drayage & Trucking", desc: "Private fleet for heavy haul.", img: "/images/trucking/trucking2.webp" }
      ]
    },
    {
      title: "Warehousing",
      description: "Secure staging and storage.",
      services: [
        { title: "Bonded Storage", desc: "Customs compliant staging areas.", img: "/images/facilitiesstorage/Secure Facilities1.webp" },
        { title: "Inventory Management", desc: "Digital tracking and reporting.", img: "/images/warehousemanagement/warehousepackaging2.webp" },
        { title: "Facility Relocation", desc: "Turnkey factory moves.", img: "/images/facilityrelocation/facilityrelocation].webp" }
      ]
    }
  ];

  return (
    <>
      <section className="pt-32 pb-16 bg-zinc-950 border-b border-zinc-900">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 className="text-5xl md:text-7xl font-black text-white uppercase tracking-tighter mb-6">Our Services</h1>
          <p className="text-xl text-zinc-400 max-w-3xl leading-relaxed">
            End-to-end industrial logistics. From precision packing of delicate instrumentation to the transloading of massive refinery components.
          </p>
        </div>
      </section>

      {categories.map((cat, idx) => (
        <SectionLayout key={idx} title={cat.title} subtitle={cat.description} dark={idx % 2 !== 0}>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-8">
            {cat.services.map((svc, i) => (
              <ServiceCard 
                key={i}
                title={svc.title}
                description={svc.desc}
                image={svc.img}
                link={`/services/${svc.title.toLowerCase().replace(/ /g, '-')}`}
              />
            ))}
          </div>
        </SectionLayout>
      ))}

      <SectionLayout dark>
        <div className="bg-morris-red p-12 md:p-20 text-center relative overflow-hidden">
          <div className="absolute inset-0 bg-[url('/images/warehousemanagement/warehousepackaging2.webp')] opacity-10 bg-cover bg-center mix-blend-multiply"></div>
          <div className="relative z-10">
            <h2 className="text-4xl md:text-5xl font-black uppercase tracking-tighter text-white mb-6">Need a custom solution?</h2>
            <p className="text-white/80 text-lg mb-10 max-w-2xl mx-auto">Our engineering team can design specialized packing and transport protocols for highly sensitive or unusual cargo.</p>
            <a href="/contact" className="inline-block bg-zinc-950 text-white px-10 py-5 font-black uppercase tracking-widest hover:bg-black transition-colors">
              Contact Engineering
            </a>
          </div>
        </div>
      </SectionLayout>
    </>
  );
}
