"""
Custom topology for Mininet, generated by GraphML-Topo-to-Mininet-Network-Generator.
"""

from mininet.topo import Topo

class GeneratedTopo( Topo ):
    "Internet Topology Zoo Specimen."

    def __init__( self ):
        "Create a topology."

        # Initialize Topology
        Topo.__init__( self )
        CHE = self.addSwitch( 's0' )
        LEI = self.addSwitch( 's1' )
        ADH = self.addSwitch( 's2' )
        DRE = self.addSwitch( 's3' )
        GSI = self.addSwitch( 's4' )
        HEI = self.addSwitch( 's5' )
        JEN = self.addSwitch( 's6' )
        ILM = self.addSwitch( 's7' )
        DeCix = self.addSwitch( 's8' )
        Geant = self.addSwitch( 's9' )
        FZK = self.addSwitch( 's10' )
        STU = self.addSwitch( 's11' )
        DeCix = self.addSwitch( 's12' )
        Telia = self.addSwitch( 's13' )
        BIE = self.addSwitch( 's14' )
        Telekom = self.addSwitch( 's15' )
        GOE = self.addSwitch( 's16' )
        BRE = self.addSwitch( 's17' )
        WUP = self.addSwitch( 's18' )
        BIR = self.addSwitch( 's19' )
        BON = self.addSwitch( 's20' )
        MAR = self.addSwitch( 's21' )
        GIE = self.addSwitch( 's22' )
        KAS = self.addSwitch( 's23' )
        PAD = self.addSwitch( 's24' )
        EWE = self.addSwitch( 's25' )
        Telekom = self.addSwitch( 's26' )
        MUE = self.addSwitch( 's27' )
        SAA = self.addSwitch( 's28' )
        GC = self.addSwitch( 's29' )
        DES = self.addSwitch( 's30' )
        HAM = self.addSwitch( 's31' )
        KIE = self.addSwitch( 's32' )
        ROS = self.addSwitch( 's33' )
        MAG = self.addSwitch( 's34' )
        BRA = self.addSwitch( 's35' )
        KAI = self.addSwitch( 's36' )
        GRE = self.addSwitch( 's37' )
        DOR = self.addSwitch( 's38' )
        BOC = self.addSwitch( 's39' )
        FHM = self.addSwitch( 's40' )
        REG = self.addSwitch( 's41' )
        AUG = self.addSwitch( 's42' )
        GAR = self.addSwitch( 's43' )
        DUI = self.addSwitch( 's44' )
        FZJ = self.addSwitch( 's45' )
        AAC = self.addSwitch( 's46' )
        WUE = self.addSwitch( 's47' )
        TUB = self.addSwitch( 's48' )
        HUB = self.addSwitch( 's49' )
        HAN = self.addSwitch( 's50' )
        FRA = self.addSwitch( 's51' )
        POT = self.addSwitch( 's52' )
        ERL = self.addSwitch( 's53' )
        BAY = self.addSwitch( 's54' )
        FFO = self.addSwitch( 's55' )
        ZIB = self.addSwitch( 's56' )
        ZEU = self.addSwitch( 's57' )

        #HOSTS (put here if needed)
        # dont forget to add edges afterwards!
        # Hamburg - Garching
        HAM_h = self.addHost( 'h1' )
        GAR_h = self.addHost( 'h2' )

        self.addLink( HAM , HAM_h )
        self.addLink( GAR , GAR_h )

        # ADD EDGES
        self.addLink( CHE , LEI, port1=None, port2=None, bw=, delay='0.298077704142ms')
        self.addLink( CHE , DRE, port1=None, port2=None, bw=, delay='0.322365195402ms')
        self.addLink( LEI , ERL, port1=None, port2=None, bw=, delay='0.999726235212ms')
        self.addLink( LEI , JEN, port1=None, port2=None, bw=, delay='0.304663741178ms')
        self.addLink( LEI , Telekom, port1=None, port2=None, bw=, delay='0.177188075451ms')
        self.addLink( ADH , ZIB, port1=None, port2=None, bw=, delay='0.0ms')
        self.addLink( ADH , HUB, port1=None, port2=None, bw=, delay='0.0ms')
        self.addLink( DRE , POT, port1=None, port2=None, bw=, delay='0.611196404787ms')
        self.addLink( DRE , ERL, port1=None, port2=None, bw=, delay='1.36511770402ms')
        self.addLink( GSI , FRA, port1=None, port2=None, bw=, delay='0.120153551776ms')
        self.addLink( GSI , HEI, port1=None, port2=None, bw=, delay='0.224591638201ms')
        self.addLink( HEI , FZK, port1=None, port2=None, bw=, delay='0.206100579927ms')
        self.addLink( JEN , ILM, port1=None, port2=None, bw=, delay='0.305112206139ms')
        self.addLink( ILM , ERL, port1=None, port2=None, bw=, delay='0.531397405368ms')
        self.addLink( DeCix , FRA, port1=None, port2=None, bw=, delay='1.07425900065ms')
        self.addLink( Geant , FRA, port1=None, port2=None, bw=, delay='1.07425900065ms')
        self.addLink( FZK , STU, port1=None, port2=None, bw=, delay='0.123846482309ms')
        self.addLink( FZK , FRA, port1=None, port2=None, bw=, delay='0.545310550152ms')
        self.addLink( FZK , KAI, port1=None, port2=None, bw=, delay='0.257654222135ms')
        self.addLink( STU , GAR, port1=None, port2=None, bw=, delay='0.183710390854ms')
        self.addLink( DeCix , POT, port1=None, port2=None, bw=, delay='1.21589909521ms')
        self.addLink( Telia , POT, port1=None, port2=None, bw=, delay='1.21589909521ms')
        self.addLink( BIE , PAD, port1=None, port2=None, bw=, delay='0.151235973103ms')
        self.addLink( BIE , HAN, port1=None, port2=None, bw=, delay='0.239411525498ms')
        self.addLink( BIE , MUE, port1=None, port2=None, bw=, delay='0.0749935777704ms')
        self.addLink( GOE , HAN, port1=None, port2=None, bw=, delay='0.403219149905ms')
        self.addLink( GOE , KAS, port1=None, port2=None, bw=, delay='0.132198343422ms')
        self.addLink( BRE , EWE, port1=None, port2=None, bw=, delay='0.285174357757ms')
        self.addLink( BRE , HAN, port1=None, port2=None, bw=, delay='0.466716654548ms')
        self.addLink( BRE , HAM, port1=None, port2=None, bw=, delay='0.613075736052ms')
        self.addLink( WUP , BIR, port1=None, port2=None, bw=, delay='0.177529497718ms')
        self.addLink( WUP , DOR, port1=None, port2=None, bw=, delay='0.132208980425ms')
        self.addLink( BIR , FRA, port1=None, port2=None, bw=, delay='0.866363974909ms')
        self.addLink( BIR , BON, port1=None, port2=None, bw=, delay='0.114396168803ms')
        self.addLink( BON , AAC, port1=None, port2=None, bw=, delay='0.43021086546ms')
        self.addLink( MAR , GIE, port1=None, port2=None, bw=, delay='0.123927107746ms')
        self.addLink( MAR , KAS, port1=None, port2=None, bw=, delay='0.335776873611ms')
        self.addLink( GIE , FRA, port1=None, port2=None, bw=, delay='0.226423040499ms')
        self.addLink( KAS , PAD, port1=None, port2=None, bw=, delay='0.212992035908ms')
        self.addLink( EWE , MUE, port1=None, port2=None, bw=, delay='0.593000769253ms')
        self.addLink( Telekom , HAN, port1=None, port2=None, bw=, delay='0.65116824746ms')
        self.addLink( MUE , DUI, port1=None, port2=None, bw=, delay='0.239436899338ms')
        self.addLink( SAA , FRA, port1=None, port2=None, bw=, delay='0.726207753593ms')
        self.addLink( SAA , KAI, port1=None, port2=None, bw=, delay='0.237226880719ms')
        self.addLink( GC , FRA, port1=None, port2=None, bw=, delay='0.726207753593ms')
        self.addLink( DES , TUB, port1=None, port2=None, bw=, delay='1.1465338582ms')
        self.addLink( DES , HAM, port1=None, port2=None, bw=, delay='0.0ms')
        self.addLink( KIE , ROS, port1=None, port2=None, bw=, delay='0.613089850628ms')
        self.addLink( KIE , HAN, port1=None, port2=None, bw=, delay='0.95715083448ms')
        self.addLink( ROS , HAN, port1=None, port2=None, bw=, delay='1.23919188963ms')
        self.addLink( ROS , GRE, port1=None, port2=None, bw=, delay='0.451874040959ms')
        self.addLink( MAG , BRA, port1=None, port2=None, bw=, delay='0.198596354707ms')
        self.addLink( MAG , POT, port1=None, port2=None, bw=, delay='0.286623903897ms')
        self.addLink( BRA , HAN, port1=None, port2=None, bw=, delay='0.181955327902ms')
        self.addLink( KAI , FRA, port1=None, port2=None, bw=, delay='0.500429501646ms')
        self.addLink( GRE , POT, port1=None, port2=None, bw=, delay='0.833384976554ms')
        self.addLink( DOR , BOC, port1=None, port2=None, bw=, delay='0.0404988498769ms')
        self.addLink( BOC , DUI, port1=None, port2=None, bw=, delay='0.0384340170956ms')
        self.addLink( FHM , REG, port1=None, port2=None, bw=, delay='0.410717758791ms')
        self.addLink( FHM , GAR, port1=None, port2=None, bw=, delay='0.0571389176142ms')
        self.addLink( REG , ERL, port1=None, port2=None, bw=, delay='0.380251182629ms')
        self.addLink( AUG , GAR, port1=None, port2=None, bw=, delay='0.146679197743ms')
        self.addLink( AUG , ERL, port1=None, port2=None, bw=, delay='0.591013866677ms')
        self.addLink( GAR , FRA, port1=None, port2=None, bw=, delay='0.476790264006ms')
        self.addLink( DUI , HAN, port1=None, port2=None, bw=, delay='0.114794696877ms')
        self.addLink( DUI , FZJ, port1=None, port2=None, bw=, delay='0.303995280517ms')
        self.addLink( FZJ , AAC, port1=None, port2=None, bw=, delay='0.136555592075ms')
        self.addLink( AAC , FRA, port1=None, port2=None, bw=, delay='1.2185434171ms')
        self.addLink( WUE , FRA, port1=None, port2=None, bw=, delay='0.590926981844ms')
        self.addLink( WUE , ERL, port1=None, port2=None, bw=, delay='0.435614129907ms')
        self.addLink( TUB , ZIB, port1=None, port2=None, bw=, delay='0.0ms')
        self.addLink( TUB , HUB, port1=None, port2=None, bw=, delay='0.0ms')
        self.addLink( TUB , POT, port1=None, port2=None, bw=, delay='0.114412479891ms')
        self.addLink( TUB , ZEU, port1=None, port2=None, bw=, delay='0.0950223458116ms')
        self.addLink( HAN , FRA, port1=None, port2=None, bw=, delay='0.947985832412ms')
        self.addLink( HAN , POT, port1=None, port2=None, bw=, delay='0.528173527957ms')
        self.addLink( HAN , ERL, port1=None, port2=None, bw=, delay='1.10642887727ms')
        self.addLink( HAN , FFO, port1=None, port2=None, bw=, delay='0.329662720518ms')
        self.addLink( FRA , POT, port1=None, port2=None, bw=, delay='0.738212609301ms')
        self.addLink( FRA , ERL, port1=None, port2=None, bw=, delay='0.977051156896ms')
        self.addLink( POT , ERL, port1=None, port2=None, bw=, delay='0.924510931658ms')
        self.addLink( POT , BAY, port1=None, port2=None, bw=, delay='0.910912393939ms')
        self.addLink( POT , FFO, port1=None, port2=None, bw=, delay='0.342242121493ms')
        self.addLink( POT , ZIB, port1=None, port2=None, bw=, delay='0.114412479891ms')
        self.addLink( ERL , BAY, port1=None, port2=None, bw=, delay='0.297042828821ms')
        self.addLink( FFO , ZIB, port1=None, port2=None, bw=, delay='0.308640678658ms')
        self.addLink( ZIB , ZEU, port1=None, port2=None, bw=, delay='0.0950223458116ms')


topos = { 'generated': ( lambda: GeneratedTopo() ) }
