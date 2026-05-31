import { Link } from 'react-router-dom'
import heroImage from '../assets/trnava-university-BEEyeib-am8-unsplash.jpg'

export default function Hero() {
  return (
    <section
      className="relative h-screen flex items-center overflow-hidden"
    >

      
      <img
        src={heroImage}
        alt="Livros e leitura"
        className="absolute inset-0 w-full h-full object-cover"
      />

      
      <div className="absolute inset-0 bg-black/50"></div>

     
      <div className="relative z-10 max-w-xl text-white px-10 md:px-20">

        <h2 className="font-[Gloock] text-5xl md:text-6xl font-bold mb-6 leading-tight">
          Transformando vidas através da leitura
        </h2>

        <p className="mb-8 text-lg leading-relaxed">
          Nossa missão é promover a inclusão e a justiça social através do incentivo à leitura, educação, cultura e a preservação do meio ambiente.
          Você pode contribuir com nossos projetos.
        </p>

        <div className="flex gap-4">

          
          <Link to="/contato">
            <button className="font-[Gloock] bg-white text-[#1B56AE] px-6 py-3 rounded-xl shadow hover:bg-[#1B56AE] hover:text-white hover:shadow-xl transition duration-300">
              Doar
            </button>
          </Link>

         
          <a
            href="https://www.facebook.com/llivroemmovimento"
            target="_blank"
            rel="noopener noreferrer"
          >
            <button className="font-[Gloock] bg-white text-[#1B56AE] px-6 py-3 rounded-xl shadow hover:bg-[#1B56AE] hover:text-white hover:shadow-xl transition duration-300">
              Contato
            </button>
          </a>

        </div>

      </div>

    </section>
  )
}