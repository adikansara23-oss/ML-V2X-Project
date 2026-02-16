column_taxonomy = {
    'timestamp': [
        'timestamp',
        # Note: 'time[s]' also exists but has 26.6% missing - likely redundant
    ],
    
    'radio_metrics': [
        # Signal quality metrics from serving cell
        'serving_cell_snr_1',      # Signal-to-Noise Ratio
        'serving_cell_rssi_1',     # Received Signal Strength Indicator
        'serving_cell_rsrq_1',     # Reference Signal Received Quality
        'serving_cell_rsrp_1',     # Reference Signal Received Power
        'serving_cell_id',
        'E-ARFCN',                 # Frequency channel
        'Number of Neighbor Cells',
        'Number of Detected Cells',
        'RSRQ(dB)',               # Alternative RSRQ measurement
        'RSRP(dBm)',              # Alternative RSRP measurement
    ],
    
    'network_qos': [
        # Uplink QoS metrics
        'delay_std_UL',            # Delay standard deviation
        'delay_mean_UL',           # Mean delay
        'jitter_UL',               # Jitter (delay variation)
        
        # Downlink QoS metrics
        'delay_std_DL',
        'delay_mean_DL',
        'jitter_DL',
        
        # Ping metrics
        'ping_size_bytes',
        'ping_ms',                 # Ping latency in milliseconds
        'ttl',                     # Time to live
        'icmp_seq',                # ICMP sequence number
        
        # Client/Server jitter
        'jitter_client',
        'jitter_server',
    ],
    
    'traffic_kpis': [
        # Uplink traffic
        'throughput_UL',           # Uplink throughput
        'target_UL',               # Target uplink rate
        'cell_load_UL',            # Cell load uplink
        'UE_UL',                   # User Equipment uplink metric
        
        # Downlink traffic
        'throughput_DL',           # Downlink throughput
        'target_DL',               # Target downlink rate
        'cell_load_DL',            # Cell load downlink
        'UE_DL',                   # User Equipment downlink metric
        
        # Data rates
        'datarate_client',
        'datarate_server',
    ],
    
    'vehicle_telemetry': [
        # Position (3D coordinates)
        'position_x',
        'position_y',
        'position_z',
        
        # GPS coordinates
        'Latitude',
        'Longitude',
        
        # Orientation (quaternion)
        'orientation_x',
        'orientation_y',
        'orientation_z',
        'orientation_w',
        
        # Linear velocity/twist
        'twist_linear_x',
        'twist_linear_y',
        'twist_linear_z',
        
        # Angular velocity
        'twist_angular_x',
        'twist_angular_y',
        'twist_angular_z',
        
        # Radio environment
        'distance_to_bs',          # Distance to base station
        'line_of_sight',           # Line of sight indicator
        'obstacles_sum',           # Number of obstacles
    ],
    
    'identifiers': [
        # Device identifiers
        'device_id',
        'device_id_server',
        'device_id_client',
        'meas_id',                 # Measurement ID
        
        # Network identifiers
        'port_local_client',
        'port_remote_client',
        'port_local_server',
        'port_remote_server',
        
        # File/session identifier
        'bag_file',                # ROS bag file identifier
    ],
    
    'technical_metadata': [
        # These are mostly low-level LTE protocol parameters
        # Prefixed with "Ignored_" - likely not useful for imputation
        # All have ~22.8% missing
        
        'Ignored_CSI-RS Exist',
        'Ignored_RhoB/RhoA',
        'Ignored_PB',
        'Ignored_ZP CSI-RS Exist',
        'Ignored_SCH1 Memory Map Mode',
        'Ignored_Traffic to Pilot Ratio Data',
        'Ignored_Transport Block Size Stream 1',
        'Ignored_SCH0 Memory Map Mode',
        'Ignored_CSI-RS Symbol Skipped',
        'Ignored_Strong ICell ID',
        'Ignored_Qice Enable Mode',
        'Ignored_Qice Skip Reason',
        'Ignored_Csf Dual Rnn Sel',
        'Ignored_Plq Num Enabled Rd Groups',
        'Ignored_BMOD FD Sym Index',
        'Ignored_Plg Num Loaded Rb Groups',
        'Ignored_Qed Mode',
        'Ignored_Transport Block Size Stream 0',
        'Ignored_UERS Port Enabled',
        'log_msg_len',
        'Ignored_System Frame Number',
        'Ignored_RB Allocation Slot 1[1]',
        'index',
        'Version',
        'Num of Records',
        'Ignored_Serving Cell ID',
        'Ignored_Sub-frame Number',
        'Ignored_PDSCH RNTIl ID',
        'Ignored_MU Receiver Mode',
        'Ignored_PMI Index',
        'Ignored_RB Allocation Slot 0[0]',
        'Ignored_RB Allocation Slot 0[1]',
        'Ignored_RB Allocation Slot 1[0]',
        'index_rs_intra_all',
        'Sub-frame Number',
        'log_msg_len_rs_intra_all',
        'Version_rs_intra_all',
    ],
}