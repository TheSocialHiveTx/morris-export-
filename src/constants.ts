import { LucideIcon, Box, Construction, Container, Shield, Truck, Factory, Warehouse, Package, AlertTriangle, ClipboardList, CircleDot, Cpu } from 'lucide-react';

export interface Service {
  id: string;
  title: string;
  slug: string;
  icon: LucideIcon;
  description: string;
  content: string;
}

export const SERVICES: Service[] = [
  {
    id: 'custom-crating',
    title: 'Custom Crating',
    slug: 'custom-crating',
    icon: Box,
    description: 'Specialized crating solutions for any size or weight.',
    content: 'Our custom crating services ensure your cargo is protected during transit with engineered solutions tailored to your specific needs.'
  },
  {
    id: 'crane',
    title: 'Crane Services',
    slug: 'crane',
    icon: Construction,
    description: 'Heavy lifting and positioning services.',
    content: 'Professional crane services for heavy equipment handling and precise positioning in challenging environments.'
  },
  {
    id: 'containerization',
    title: 'Containerization',
    slug: 'containerization',
    icon: Container,
    description: 'Efficient loading and securing of export containers.',
    content: 'Expert container loading, blocking, and bracing to maximize space and ensure cargo stability.'
  },
  {
    id: 'wrap-protection',
    title: 'Wrap & Protection',
    slug: 'wrap-protection',
    icon: Shield,
    description: 'Advanced shrink wrapping and moisture protection.',
    content: 'VCI protection and heavy-duty shrink wrapping to safeguard equipment from the elements.'
  },
  {
    id: 'trucking-drayage',
    title: 'Trucking & Drayage',
    slug: 'trucking-drayage',
    icon: Truck,
    description: 'Reliable transport and port delivery services.',
    content: 'Seamless trucking and drayage services connecting your cargo to major ports and domestic destinations.'
  },
  {
    id: 'equipment-facility-relocation',
    title: 'Equipment & Facility Relocation',
    slug: 'equipment-facility-relocation',
    icon: Factory,
    description: 'Turnkey solutions for moving entire facilities.',
    content: 'Comprehensive planning and execution for relocating industrial equipment and entire manufacturing plants.'
  },
  {
    id: 'facilities-warehouse-storage',
    title: 'Facilities, Warehouse & Storage',
    slug: 'facilities-warehouse-storage',
    icon: Warehouse,
    description: 'Secure short and long-term storage solutions.',
    content: 'State-of-the-art warehouse facilities providing secure storage and inventory management.'
  },
  {
    id: 'on-site-packing-services',
    title: 'On-Site Packing Services',
    slug: 'on-site-packing-services',
    icon: Package,
    description: 'We bring our expertise directly to your facility.',
    content: 'Mobile packing teams equipped to handle crating and securing at your location.'
  },
  {
    id: 'hazardous-packaging',
    title: 'Hazardous Packaging',
    slug: 'hazardous-packaging',
    icon: AlertTriangle,
    description: 'Certified handling of dangerous goods.',
    content: 'UN-certified packaging and documentation for hazardous materials and dangerous goods.'
  },
  {
    id: 'customer-warehouse-management',
    title: 'Customer Warehouse Management',
    slug: 'customer-warehouse-management',
    icon: ClipboardList,
    description: 'Optimizing your internal logistics.',
    content: 'Professional management of your warehouse operations to improve efficiency and accuracy.'
  },
  {
    id: 'pipe-protection-bolsters',
    title: 'Pipe Protection & Bolsters',
    slug: 'pipe-protection-bolsters',
    icon: CircleDot,
    description: 'Specialized solutions for the oil & gas industry.',
    content: 'Custom bolsters and protection systems for pipes and tubular goods.'
  },
  {
    id: 'm-pact-technology-software',
    title: 'M-Pact Technology & Software',
    slug: 'm-pact-technology-software',
    icon: Cpu,
    description: 'Proprietary tracking and management software.',
    content: 'Real-time visibility and reporting through our custom M-Pact logistics software platform.'
  }
];
