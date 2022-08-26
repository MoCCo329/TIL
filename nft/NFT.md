



### MetaMask

블록체인 네트워크를 사용할 수 있도록 계정의 개인키를 관리하는 프로그램을 지갑(Wallet)이라 한다.

개인키는 256bit의 무작위 숫자이며 이를 64자리의 Hex값으로 인코딩한다.

타원곡선전자서명 알고리즘(ECDSA, secp256k1)을 사용하여 공개키를 생성한다.

Keccak-256 hashing function을 이용해 새로운 값으로 변환

변환한 값의 마지막 20byte(40자리)를 계정 주소로 한다.



Ropsten 테스트 네트워크를 사용한다.

ropsten faucet을 이용해 테스트 이더리움을 받는다. 



### Provider API

클라이언트를 통해 이더리움 네트워크에 접근할 수 있도록 제공된 Javascript 객체



### Smart Contract

디지털 형식으로 명시된 서약(Commitment)들의 집합으로 단순 컴퓨터 프로그램이다.

법적 맥락은 없으며, 자연어의 모호함을 피하기 위해 프로그래밍 언어로 만든 서약이다.

블록체인에서의 정의는 불변의 컴퓨터 프로그램을 말한다. 즉 한번 배포되면 변경이 불가한 프로그램이며, EVM(Ethereum Virtual Machine) 위에서 동작한다.

Solidity, LLL, Viper, Assembly 같은 언어를 이용한다.



Smart Contract code를 작성하면 EVM Bytecode, ABI json interface가 생성된다. 트랜젝션 data에 bytecode가 담기고 이를 서명하면 바이트코드가 EVM에서 실행되어 전파된다.

배포된 컨트랙트 주소(CA contract Address)와 ABI를 통해 함수 호출이 가능하다.



### Smart Contract 배포

.sol은 solidity 언어, Remix IDE를 이용해 실습한다.

컴파일을 완료하면 artifacts 폴더에 json 파일 두개가 생성된다. 이것이 Bytecode와 ABI이다.

배포를 하면 배포 주소가 생성된다.