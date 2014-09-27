#
# Supported handle types
#
MBUS_HANDLE_TYPE_TCP	= 0
MBUS_HANDLE_TYPE_SERIAL	= 1

#
# Resultcodes for mbus_recv_frame
#
MBUS_RECV_RESULT_OK	= 0
MBUS_RECV_RESULT_ERROR	= -1
MBUS_RECV_RESULT_INVALID	= -2
MBUS_RECV_RESULT_TIMEOUT	= -3
MBUS_RECV_RESULT_RESET	= -4

#------------------------------------------------------------------------------
# MBUS FRAME DATA FORMATS
#

# DATA RECORDS
MBUS_DIB_DIF_WITHOUT_EXTENSION     = 0x7F
MBUS_DIB_DIF_EXTENSION_BIT         = 0x80
MBUS_DIB_VIF_WITHOUT_EXTENSION     = 0x7F
MBUS_DIB_VIF_EXTENSION_BIT         = 0x80
MBUS_DIB_DIF_MANUFACTURER_SPECIFIC = 0x0F
MBUS_DIB_DIF_MORE_RECORDS_FOLLOW   = 0x1F
MBUS_DIB_DIF_IDLE_FILLER           = 0x2F

#------------------------------------------------------------------------------
# FRAME types
#
MBUS_FRAME_TYPE_ANY                = 0x00
MBUS_FRAME_TYPE_ACK                = 0x01
MBUS_FRAME_TYPE_SHORT              = 0x02
MBUS_FRAME_TYPE_CONTROL            = 0x03
MBUS_FRAME_TYPE_LONG               = 0x04

MBUS_FRAME_ACK_BASE_SIZE           = 1
MBUS_FRAME_SHORT_BASE_SIZE         = 5
MBUS_FRAME_CONTROL_BASE_SIZE       = 9
MBUS_FRAME_LONG_BASE_SIZE          = 9

MBUS_FRAME_BASE_SIZE_ACK           = 1
MBUS_FRAME_BASE_SIZE_SHORT         = 5
MBUS_FRAME_BASE_SIZE_CONTROL       = 9
MBUS_FRAME_BASE_SIZE_LONG          = 9

MBUS_FRAME_FIXED_SIZE_ACK          = 1
MBUS_FRAME_FIXED_SIZE_SHORT        = 5
MBUS_FRAME_FIXED_SIZE_CONTROL      = 6
MBUS_FRAME_FIXED_SIZE_LONG         = 6

#
# Frame start/stop bits
#
MBUS_FRAME_ACK_START               = 0xE5
MBUS_FRAME_SHORT_START             = 0x10
MBUS_FRAME_CONTROL_START           = 0x68
MBUS_FRAME_LONG_START              = 0x68
MBUS_FRAME_STOP                    = 0x16

#
#
#
MBUS_MAX_PRIMARY_SLAVES            = 250

#
# Control field
#
MBUS_CONTROL_FIELD_DIRECTION       = 0x07
MBUS_CONTROL_FIELD_FCB             = 0x06
MBUS_CONTROL_FIELD_ACD             = 0x06
MBUS_CONTROL_FIELD_FCV             = 0x05
MBUS_CONTROL_FIELD_DFC             = 0x05
MBUS_CONTROL_FIELD_F3              = 0x04
MBUS_CONTROL_FIELD_F2              = 0x03
MBUS_CONTROL_FIELD_F1              = 0x02
MBUS_CONTROL_FIELD_F0              = 0x01

MBUS_CONTROL_MASK_SND_NKE          = 0x40
MBUS_CONTROL_MASK_SND_UD           = 0x53
MBUS_CONTROL_MASK_REQ_UD2          = 0x5B
MBUS_CONTROL_MASK_REQ_UD1          = 0x5A
MBUS_CONTROL_MASK_RSP_UD           = 0x08

MBUS_CONTROL_MASK_FCB                  = 0x20
MBUS_CONTROL_MASK_FCV                  = 0x10

MBUS_CONTROL_MASK_ACD                  = 0x20
MBUS_CONTROL_MASK_DFC                  = 0x10

MBUS_CONTROL_MASK_DIR                  = 0x40
MBUS_CONTROL_MASK_DIR_M2S              = 0x40
MBUS_CONTROL_MASK_DIR_S2M              = 0x00

#
# Address field
#
MBUS_ADDRESS_BROADCAST_REPLY            = 0xFE
MBUS_ADDRESS_BROADCAST_NOREPLY          = 0xFF
MBUS_ADDRESS_NETWORK_LAYER              = 0xFD

#
# Control field
#
MBUS_CONTROL_INFO_DATA_SEND             = 0x51
MBUS_CONTROL_INFO_DATA_SEND_MSB	        = 0x55
MBUS_CONTROL_INFO_SELECT_SLAVE	        = 0x52
MBUS_CONTROL_INFO_SELECT_SLAVE_MSB	    = 0x56
MBUS_CONTROL_INFO_APPLICATION_RESET	    = 0x50
MBUS_CONTROL_INFO_SYNC_ACTION	        = 0x54
MBUS_CONTROL_INFO_SET_BAUDRATE_300	    = 0xB8
MBUS_CONTROL_INFO_SET_BAUDRATE_600	    = 0xB9
MBUS_CONTROL_INFO_SET_BAUDRATE_1200	    = 0xBA
MBUS_CONTROL_INFO_SET_BAUDRATE_2400	    = 0xBB
MBUS_CONTROL_INFO_SET_BAUDRATE_4800	    = 0xBC
MBUS_CONTROL_INFO_SET_BAUDRATE_9600     = 0xBD
MBUS_CONTROL_INFO_SET_BAUDRATE_19200    = 0xBE
MBUS_CONTROL_INFO_SET_BAUDRATE_38400    = 0xBF
MBUS_CONTROL_INFO_REQUEST_RAM_READ      = 0xB1
MBUS_CONTROL_INFO_SEND_USER_DATA        = 0xB2
MBUS_CONTROL_INFO_INIT_TEST_CALIB       = 0xB3
MBUS_CONTROL_INFO_EEPROM_READ           = 0xB4
MBUS_CONTROL_INFO_SW_TEST_START         = 0xB6

MBUS_CONTROL_INFO_ERROR_GENERAL         = 0x70
MBUS_CONTROL_INFO_STATUS_ALARM          = 0x71

MBUS_CONTROL_INFO_RESP_FIXED            = 0x73
MBUS_CONTROL_INFO_RESP_FIXED_MSB        = 0x77

MBUS_CONTROL_INFO_RESP_VARIABLE         = 0x72
MBUS_CONTROL_INFO_RESP_VARIABLE_MSB     = 0x76

#
# Data bits
#
MBUS_DATA_FIXED_STATUS_FORMAT_MASK	= 0x80
MBUS_DATA_FIXED_STATUS_FORMAT_BCD	= 0x00
MBUS_DATA_FIXED_STATUS_FORMAT_INT	= 0x80
MBUS_DATA_FIXED_STATUS_DATE_MASK	= 0x40
MBUS_DATA_FIXED_STATUS_DATE_STORED	= 0x40
MBUS_DATA_FIXED_STATUS_DATE_CURRENT	= 0x00


#
# Data Record Field
#
MBUS_DATA_RECORD_DIF_MASK_INST	= 0x00
MBUS_DATA_RECORD_DIF_MASK_MIN	= 0x10

MBUS_DATA_RECORD_DIF_MASK_TYPE_INT32	= 0x04
MBUS_DATA_RECORD_DIF_MASK_DATA	= 0x0F
MBUS_DATA_RECORD_DIF_MASK_FUNCTION	= 0x30
MBUS_DATA_RECORD_DIF_MASK_STORAGE_NO	= 0x40
MBUS_DATA_RECORD_DIF_MASK_EXTENTION	= 0x80
MBUS_DATA_RECORD_DIF_MASK_NON_DATA	= 0xF0

MBUS_DATA_RECORD_DIFE_MASK_STORAGE_NO	= 0x0F
MBUS_DATA_RECORD_DIFE_MASK_TARIFF	= 0x30
MBUS_DATA_RECORD_DIFE_MASK_DEVICE	= 0x40
MBUS_DATA_RECORD_DIFE_MASK_EXTENSION	= 0x80

#
# GENERAL APPLICATION ERRORS
#
MBUS_ERROR_DATA_UNSPECIFIED	= 0x00
MBUS_ERROR_DATA_UNIMPLEMENTED_CI	= 0x01
MBUS_ERROR_DATA_BUFFER_TOO_LONG	= 0x02
MBUS_ERROR_DATA_TOO_MANY_RECORDS	= 0x03
MBUS_ERROR_DATA_PREMATURE_END	= 0x04
MBUS_ERROR_DATA_TOO_MANY_DIFES	= 0x05
MBUS_ERROR_DATA_TOO_MANY_VIFES	= 0x06
MBUS_ERROR_DATA_RESERVED	= 0x07
MBUS_ERROR_DATA_APPLICATION_BUSY	= 0x08
MBUS_ERROR_DATA_TOO_MANY_READOUTS	= 0x09

#
# FIXED DATA FLAGS
#

#
# VARIABLE DATA FLAGS
#
MBUS_VARIABLE_DATA_MEDIUM_OTHER	= 0x00
MBUS_VARIABLE_DATA_MEDIUM_OIL	= 0x01
MBUS_VARIABLE_DATA_MEDIUM_ELECTRICITY	= 0x02
MBUS_VARIABLE_DATA_MEDIUM_GAS	= 0x03
MBUS_VARIABLE_DATA_MEDIUM_HEAT_OUT	= 0x04
MBUS_VARIABLE_DATA_MEDIUM_STEAM	= 0x05
MBUS_VARIABLE_DATA_MEDIUM_HOT_WATER	= 0x06
MBUS_VARIABLE_DATA_MEDIUM_WATER	= 0x07
MBUS_VARIABLE_DATA_MEDIUM_HEAT_COST	= 0x08
MBUS_VARIABLE_DATA_MEDIUM_COMPR_AIR	= 0x09
MBUS_VARIABLE_DATA_MEDIUM_COOL_OUT	= 0x0A
MBUS_VARIABLE_DATA_MEDIUM_COOL_IN	= 0x0B
MBUS_VARIABLE_DATA_MEDIUM_HEAT_IN	= 0x0C
MBUS_VARIABLE_DATA_MEDIUM_HEAT_COOL	= 0x0D
MBUS_VARIABLE_DATA_MEDIUM_BUS	= 0x0E
MBUS_VARIABLE_DATA_MEDIUM_UNKNOWN	= 0x0F
MBUS_VARIABLE_DATA_MEDIUM_COLD_WATER	= 0x16
MBUS_VARIABLE_DATA_MEDIUM_DUAL_WATER	= 0x17
MBUS_VARIABLE_DATA_MEDIUM_PRESSURE	= 0x18
MBUS_VARIABLE_DATA_MEDIUM_ADC	= 0x19

MBUS_FRAME_DATA_LENGTH	= 252
MBUS_DATA_VARIABLE_HEADER_LENGTH	= 12

MBUS_DATA_FIXED_LENGTH	= 16
MBUS_DATA_TYPE_FIXED	= 1
MBUS_DATA_TYPE_VARIABLE	= 2
MBUS_DATA_TYPE_ERROR	= 3