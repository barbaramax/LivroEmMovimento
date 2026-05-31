import { Link } from 'react-router-dom'
import missionImage from '../assets/foto nossa missao.jpg'

export default function MissionSection() {
  return (
    <section className="px-10 py-20 flex flex-col md:flex-row items-center gap-16">

  
      <img
        src={missionImage}
        alt="Nossa missão"
        className="w-full md:w-[500px] h-[400px] object-cover rounded-[35px] shadow-2xl"
      />

 
      <div className="max-w-2xl">

        <h2 className="font-[Gloock] text-5xl font-bold mb-6">
          Nossa missão
        </h2>

        <p className="text-gray-700 text-lg leading-relaxed mb-8">
          O Livro em Movimento nasceu da vontade de democratizar o acesso à
          leitura e educação.
        </p>

     
        <Link to="/sobre">
          <button className="bg-[#1B56AE] text-white px-8 py-3 rounded-xl shadow hover:bg-white hover:text-[#1B56AE] hover:shadow-xl transition duration-300">
            Conheça nossa história
          </button>
        </Link>

      </div>

    </section>
  )
}