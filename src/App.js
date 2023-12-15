import TradingViewWidget from './TradingViewWidget';
import './App.css';
import LogoBlack from './images/Logo_Black.png'

export default function App() {

    return (
        <body>
            <header>
                <img src={LogoBlack} className="logoHeader" onClick={() => window.location.reload()}/>
                <div className="helloUser">
                    <h2>Hello Maxime !</h2>
                    <p>Belle journée n'est-ce pas ?</p>
                </div>
            </header>
            <main>
                <div className="blocFluxActuel">
                    <div className="fluxActuel">
                        <h2>Flux actuel ·</h2><h3>Gold</h3>
                    </div>
                    <div className="tradingViewWidget">
                        <TradingViewWidget/>
                    </div>
                    <button className="btnGenererPrediction">Générer une prédiction</button>
                </div>
                <div className="blocActions">
                    <div className="Actions Action1">
                        <h4>Gold</h4>
                    </div>
                    <div className="Actions Action2">
                        <h4>Gold</h4>
                    </div>
                    <div className="Actions Action3">
                        <h4>Gold</h4>
                    </div>
                    <div className="Actions Action4">
                        <h4>Gold</h4>
                    </div>
                    <div className="Actions Action5">
                        <h4>Gold</h4>
                    </div>
                    <div className="Actions Action6">
                        <h4>Gold</h4>
                    </div>
                </div>
                <div className="blocPrediction">
                    <div className="prediction">
                        <h2>Prédiction</h2>
                    </div>
                    <button className="btnExporterPrediction">Exporter la prédiction</button>
                </div>
                <div className="blocProfil"></div>
            </main>
        </body>
    )
}