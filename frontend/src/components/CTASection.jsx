import { Link } from 'react-router-dom'

export default function CTASection() {
  return (
    <section className="bg-blue-100 py-20 px-10 text-center">

      <h2 className="font-[Gloock] text-5xl font-bold mb-6">
        Faça Parte Dessa Transformação
      </h2>

      <p className="text-gray-700 mb-10 text-lg">
        Cada doação é uma nova oportunidade de aprendizado.
      </p>

      <div className="flex justify-center gap-6">

        <Link to="/voluntarios">
          <button className="font-[Gloock] bg-white text-[#1B56AE] px-8 py-3 rounded-xl shadow hover:bg-[#1B56AE] hover:text-white hover:shadow-xl transition duration-300">
            Seja voluntário
          </button>
        </Link>

      </div>

    </section>
  )
}