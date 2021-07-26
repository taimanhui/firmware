# Automatically generated by pb2py
# fmt: off
from trezor import utils

if __debug__:
    try:
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass

Initialize: Literal[0] = 0
Ping: Literal[1] = 1
Success: Literal[2] = 2
Failure: Literal[3] = 3
ChangePin: Literal[4] = 4
WipeDevice: Literal[5] = 5
GetEntropy: Literal[9] = 9
Entropy: Literal[10] = 10
LoadDevice: Literal[13] = 13
ResetDevice: Literal[14] = 14
Features: Literal[17] = 17
PinMatrixRequest: Literal[18] = 18
PinMatrixAck: Literal[19] = 19
Cancel: Literal[20] = 20
LockDevice: Literal[24] = 24
ApplySettings: Literal[25] = 25
ButtonRequest: Literal[26] = 26
ButtonAck: Literal[27] = 27
ApplyFlags: Literal[28] = 28
BackupDevice: Literal[34] = 34
EntropyRequest: Literal[35] = 35
EntropyAck: Literal[36] = 36
PassphraseRequest: Literal[41] = 41
PassphraseAck: Literal[42] = 42
RecoveryDevice: Literal[45] = 45
WordRequest: Literal[46] = 46
WordAck: Literal[47] = 47
GetFeatures: Literal[55] = 55
SetU2FCounter: Literal[63] = 63
SdProtect: Literal[79] = 79
GetNextU2FCounter: Literal[80] = 80
NextU2FCounter: Literal[81] = 81
ChangeWipeCode: Literal[82] = 82
EndSession: Literal[83] = 83
DoPreauthorized: Literal[84] = 84
PreauthorizedRequest: Literal[85] = 85
CancelAuthorization: Literal[86] = 86
Deprecated_PassphraseStateRequest: Literal[77] = 77
Deprecated_PassphraseStateAck: Literal[78] = 78
FirmwareErase: Literal[6] = 6
FirmwareErase_ex: Literal[16] = 16
FirmwareUpload: Literal[7] = 7
FirmwareRequest: Literal[8] = 8
SelfTest: Literal[32] = 32
GetPublicKey: Literal[11] = 11
PublicKey: Literal[12] = 12
SignTx: Literal[15] = 15
TxRequest: Literal[21] = 21
TxAck: Literal[22] = 22
GetAddress: Literal[29] = 29
Address: Literal[30] = 30
SignMessage: Literal[38] = 38
VerifyMessage: Literal[39] = 39
MessageSignature: Literal[40] = 40
GetOwnershipId: Literal[43] = 43
OwnershipId: Literal[44] = 44
GetOwnershipProof: Literal[49] = 49
OwnershipProof: Literal[50] = 50
AuthorizeCoinJoin: Literal[51] = 51
CipherKeyValue: Literal[23] = 23
CipheredKeyValue: Literal[48] = 48
SignIdentity: Literal[53] = 53
SignedIdentity: Literal[54] = 54
GetECDHSessionKey: Literal[61] = 61
ECDHSessionKey: Literal[62] = 62
CosiCommit: Literal[71] = 71
CosiCommitment: Literal[72] = 72
CosiSign: Literal[73] = 73
CosiSignature: Literal[74] = 74
DebugLinkDecision: Literal[100] = 100
DebugLinkGetState: Literal[101] = 101
DebugLinkState: Literal[102] = 102
DebugLinkStop: Literal[103] = 103
DebugLinkLog: Literal[104] = 104
DebugLinkMemoryRead: Literal[110] = 110
DebugLinkMemory: Literal[111] = 111
DebugLinkMemoryWrite: Literal[112] = 112
DebugLinkFlashErase: Literal[113] = 113
DebugLinkLayout: Literal[9001] = 9001
DebugLinkReseedRandom: Literal[9002] = 9002
DebugLinkRecordScreen: Literal[9003] = 9003
DebugLinkShowText: Literal[9004] = 9004
DebugLinkEraseSdCard: Literal[9005] = 9005
DebugLinkWatchLayout: Literal[9006] = 9006
if not utils.BITCOIN_ONLY:
    EthereumGetPublicKey: Literal[450] = 450
    EthereumPublicKey: Literal[451] = 451
    EthereumGetAddress: Literal[56] = 56
    EthereumAddress: Literal[57] = 57
    EthereumSignTx: Literal[58] = 58
    EthereumTxRequest: Literal[59] = 59
    EthereumTxAck: Literal[60] = 60
    EthereumSignMessage: Literal[64] = 64
    EthereumVerifyMessage: Literal[65] = 65
    EthereumMessageSignature: Literal[66] = 66
    NEMGetAddress: Literal[67] = 67
    NEMAddress: Literal[68] = 68
    NEMSignTx: Literal[69] = 69
    NEMSignedTx: Literal[70] = 70
    NEMDecryptMessage: Literal[75] = 75
    NEMDecryptedMessage: Literal[76] = 76
    LiskGetAddress: Literal[114] = 114
    LiskAddress: Literal[115] = 115
    LiskSignTx: Literal[116] = 116
    LiskSignedTx: Literal[117] = 117
    LiskSignMessage: Literal[118] = 118
    LiskMessageSignature: Literal[119] = 119
    LiskVerifyMessage: Literal[120] = 120
    LiskGetPublicKey: Literal[121] = 121
    LiskPublicKey: Literal[122] = 122
    TezosGetAddress: Literal[150] = 150
    TezosAddress: Literal[151] = 151
    TezosSignTx: Literal[152] = 152
    TezosSignedTx: Literal[153] = 153
    TezosGetPublicKey: Literal[154] = 154
    TezosPublicKey: Literal[155] = 155
    StellarSignTx: Literal[202] = 202
    StellarTxOpRequest: Literal[203] = 203
    StellarGetAddress: Literal[207] = 207
    StellarAddress: Literal[208] = 208
    StellarCreateAccountOp: Literal[210] = 210
    StellarPaymentOp: Literal[211] = 211
    StellarPathPaymentOp: Literal[212] = 212
    StellarManageOfferOp: Literal[213] = 213
    StellarCreatePassiveOfferOp: Literal[214] = 214
    StellarSetOptionsOp: Literal[215] = 215
    StellarChangeTrustOp: Literal[216] = 216
    StellarAllowTrustOp: Literal[217] = 217
    StellarAccountMergeOp: Literal[218] = 218
    StellarManageDataOp: Literal[220] = 220
    StellarBumpSequenceOp: Literal[221] = 221
    StellarSignedTx: Literal[230] = 230
    CardanoSignTx: Literal[303] = 303
    CardanoGetPublicKey: Literal[305] = 305
    CardanoPublicKey: Literal[306] = 306
    CardanoGetAddress: Literal[307] = 307
    CardanoAddress: Literal[308] = 308
    CardanoSignedTx: Literal[310] = 310
    RippleGetAddress: Literal[400] = 400
    RippleAddress: Literal[401] = 401
    RippleSignTx: Literal[402] = 402
    RippleSignedTx: Literal[403] = 403
    MoneroTransactionInitRequest: Literal[501] = 501
    MoneroTransactionInitAck: Literal[502] = 502
    MoneroTransactionSetInputRequest: Literal[503] = 503
    MoneroTransactionSetInputAck: Literal[504] = 504
    MoneroTransactionInputsPermutationRequest: Literal[505] = 505
    MoneroTransactionInputsPermutationAck: Literal[506] = 506
    MoneroTransactionInputViniRequest: Literal[507] = 507
    MoneroTransactionInputViniAck: Literal[508] = 508
    MoneroTransactionAllInputsSetRequest: Literal[509] = 509
    MoneroTransactionAllInputsSetAck: Literal[510] = 510
    MoneroTransactionSetOutputRequest: Literal[511] = 511
    MoneroTransactionSetOutputAck: Literal[512] = 512
    MoneroTransactionAllOutSetRequest: Literal[513] = 513
    MoneroTransactionAllOutSetAck: Literal[514] = 514
    MoneroTransactionSignInputRequest: Literal[515] = 515
    MoneroTransactionSignInputAck: Literal[516] = 516
    MoneroTransactionFinalRequest: Literal[517] = 517
    MoneroTransactionFinalAck: Literal[518] = 518
    MoneroKeyImageExportInitRequest: Literal[530] = 530
    MoneroKeyImageExportInitAck: Literal[531] = 531
    MoneroKeyImageSyncStepRequest: Literal[532] = 532
    MoneroKeyImageSyncStepAck: Literal[533] = 533
    MoneroKeyImageSyncFinalRequest: Literal[534] = 534
    MoneroKeyImageSyncFinalAck: Literal[535] = 535
    MoneroGetAddress: Literal[540] = 540
    MoneroAddress: Literal[541] = 541
    MoneroGetWatchKey: Literal[542] = 542
    MoneroWatchKey: Literal[543] = 543
    DebugMoneroDiagRequest: Literal[546] = 546
    DebugMoneroDiagAck: Literal[547] = 547
    MoneroGetTxKeyRequest: Literal[550] = 550
    MoneroGetTxKeyAck: Literal[551] = 551
    MoneroLiveRefreshStartRequest: Literal[552] = 552
    MoneroLiveRefreshStartAck: Literal[553] = 553
    MoneroLiveRefreshStepRequest: Literal[554] = 554
    MoneroLiveRefreshStepAck: Literal[555] = 555
    MoneroLiveRefreshFinalRequest: Literal[556] = 556
    MoneroLiveRefreshFinalAck: Literal[557] = 557
    EosGetPublicKey: Literal[600] = 600
    EosPublicKey: Literal[601] = 601
    EosSignTx: Literal[602] = 602
    EosTxActionRequest: Literal[603] = 603
    EosTxActionAck: Literal[604] = 604
    EosSignedTx: Literal[605] = 605
    BinanceGetAddress: Literal[700] = 700
    BinanceAddress: Literal[701] = 701
    BinanceGetPublicKey: Literal[702] = 702
    BinancePublicKey: Literal[703] = 703
    BinanceSignTx: Literal[704] = 704
    BinanceTxRequest: Literal[705] = 705
    BinanceTransferMsg: Literal[706] = 706
    BinanceOrderMsg: Literal[707] = 707
    BinanceCancelMsg: Literal[708] = 708
    BinanceSignedTx: Literal[709] = 709
    WebAuthnListResidentCredentials: Literal[800] = 800
    WebAuthnCredentials: Literal[801] = 801
    WebAuthnAddResidentCredential: Literal[802] = 802
    WebAuthnRemoveResidentCredential: Literal[803] = 803
    BixinSeedOperate: Literal[901] = 901
    BixinMessageSE: Literal[902] = 902
    BixinReboot: Literal[903] = 903
    BixinOutMessageSE: Literal[904] = 904
    BixinBackupRequest: Literal[905] = 905
    BixinBackupAck: Literal[906] = 906
    BixinRestoreRequest: Literal[907] = 907
    BixinRestoreAck: Literal[908] = 908
    BixinVerifyDeviceRequest: Literal[909] = 909
    BixinVerifyDeviceAck: Literal[910] = 910
    BixinWhiteListRequest: Literal[911] = 911
    BixinWhiteListAck: Literal[912] = 912
    BixinLoadDevice: Literal[913] = 913
    BixinBackupDevice: Literal[914] = 914
    BixinBackupDeviceAck: Literal[915] = 915
    BixinPinInputOnDevice: Literal[10000] = 10000
DeviceInfoSettings: Literal[10001] = 10001
GetDeviceInfo: Literal[10002] = 10002
DeviceInfo: Literal[10003] = 10003
ReadSEPublicKey: Literal[10004] = 10004
SEPublicKey: Literal[10005] = 10005
WriteSEPublicCert: Literal[10006] = 10006
ReadSEPublicCert: Literal[10007] = 10007
SEPublicCert: Literal[10008] = 10008
SpiFlashWrite: Literal[10009] = 10009
SpiFlashRead: Literal[10010] = 10010
SpiFlashData: Literal[10011] = 10011
