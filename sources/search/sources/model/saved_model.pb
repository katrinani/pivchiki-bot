��	
�(�'
D
AddV2
x"T
y"T
z"T"
Ttype:
2	��
^
AssignVariableOp
resource
value"dtype"
dtypetype"
validate_shapebool( �
�
BiasAdd

value"T	
bias"T
output"T""
Ttype:
2	"-
data_formatstringNHWC:
NHWCNCHW
A
BroadcastArgs
s0"T
s1"T
r0"T"
Ttype0:
2	
Z
BroadcastTo

input"T
shape"Tidx
output"T"	
Ttype"
Tidxtype0:
2	
N
Cast	
x"SrcT	
y"DstT"
SrcTtype"
DstTtype"
Truncatebool( 
P

ComplexAbs
x"T	
y"Tout"
Ttype0:
2"
Touttype0:
2
h
ConcatV2
values"T*N
axis"Tidx
output"T"
Nint(0"	
Ttype"
Tidxtype0:
2	
8
Const
output"dtype"
valuetensor"
dtypetype
�
Conv2D

input"T
filter"T
output"T"
Ttype:	
2"
strides	list(int)"
use_cudnn_on_gpubool(",
paddingstring:
SAMEVALIDEXPLICIT""
explicit_paddings	list(int)
 "-
data_formatstringNHWC:
NHWCNCHW" 
	dilations	list(int)

,
Cos
x"T
y"T"
Ttype:

2
$
DisableCopyOnRead
resource�
R
Equal
x"T
y"T
z
"	
Ttype"$
incompatible_shape_errorbool(�
W

ExpandDims

input"T
dim"Tdim
output"T"	
Ttype"
Tdimtype0:
2	
^
Fill
dims"
index_type

value"T
output"T"	
Ttype"

index_typetype0:
2	
A
FloorDiv
x"T
y"T
z"T"
Ttype:
2	
?
FloorMod
x"T
y"T
z"T"
Ttype:
2	
�
GatherV2
params"Tparams
indices"Tindices
axis"Taxis
output"Tparams"

batch_dimsint "
Tparamstype"
Tindicestype:
2	"
Taxistype:
2	
B
GreaterEqual
x"T
y"T
z
"
Ttype:
2	
.
Identity

input"T
output"T"	
Ttype
,
Log
x"T
y"T"
Ttype:

2
�
MatMul
a"T
b"T
product"T"
transpose_abool( "
transpose_bbool( "
Ttype:
2	"
grad_abool( "
grad_bbool( 
�
MaxPool

input"T
output"T"
Ttype0:
2	"
ksize	list(int)(0"
strides	list(int)(0",
paddingstring:
SAMEVALIDEXPLICIT""
explicit_paddings	list(int)
 ":
data_formatstringNHWC:
NHWCNCHWNCHW_VECT_C
>
Maximum
x"T
y"T
z"T"
Ttype:
2	
�
MergeV2Checkpoints
checkpoint_prefixes
destination_prefix"
delete_old_dirsbool("
allow_missing_filesbool( �
>
Minimum
x"T
y"T
z"T"
Ttype:
2	
?
Mul
x"T
y"T
z"T"
Ttype:
2	�

NoOp
M
Pack
values"T*N
output"T"
Nint(0"	
Ttype"
axisint 
_
Pad

input"T
paddings"	Tpaddings
output"T"	
Ttype"
	Tpaddingstype0:
2	
C
Placeholder
output"dtype"
dtypetype"
shapeshape:
s
RFFT
input"Treal

fft_length
output"Tcomplex"
Trealtype0:
2"
Tcomplextype0:
2
f
Range
start"Tidx
limit"Tidx
delta"Tidx
output"Tidx" 
Tidxtype0:
2
	
@
ReadVariableOp
resource
value"dtype"
dtypetype�
@
RealDiv
x"T
y"T
z"T"
Ttype:
2	
E
Relu
features"T
activations"T"
Ttype:
2	
[
Reshape
tensor"T
shape"Tshape
output"T"	
Ttype"
Tshapetype0:
2	
o
	RestoreV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0�
l
SaveV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0�
?
Select
	condition

t"T
e"T
output"T"	
Ttype
A
SelectV2
	condition

t"T
e"T
output"T"	
Ttype
d
Shape

input"T&
output"out_type��out_type"	
Ttype"
out_typetype0:
2	
H
ShardedFilename
basename	
shard

num_shards
filename
a
Slice

input"T
begin"Index
size"Index
output"T"	
Ttype"
Indextype:
2	
[
Split
	split_dim

value"T
output"T*	num_split"
	num_splitint(0"	
Ttype
�
SplitV

value"T
size_splits"Tlen
	split_dim
output"T*	num_split"
	num_splitint(0"	
Ttype"
Tlentype0	:
2	
�
StatefulPartitionedCall
args2Tin
output2Tout"
Tin
list(type)("
Tout
list(type)("	
ffunc"
configstring "
config_protostring "
executor_typestring ��
@
StaticRegexFullMatch	
input

output
"
patternstring
�
StridedSlice

input"T
begin"Index
end"Index
strides"Index
output"T"	
Ttype"
Indextype:
2	"

begin_maskint "
end_maskint "
ellipsis_maskint "
new_axis_maskint "
shrink_axis_maskint 
L

StringJoin
inputs*N

output"

Nint("
	separatorstring 
<
Sub
x"T
y"T
z"T"
Ttype:
2	
�
VarHandleOp
resource"
	containerstring "
shared_namestring "

debug_namestring "
dtypetype"
shapeshape"#
allowed_deviceslist(string)
 �"serve*2.19.02v2.19.0-rc0-6-ge36baa302928��	
�
vggish/fc2/biasesVarHandleOp*
_output_shapes
: *"

debug_namevggish/fc2/biases/*
dtype0*
shape:�*"
shared_namevggish/fc2/biases
t
%vggish/fc2/biases/Read/ReadVariableOpReadVariableOpvggish/fc2/biases*
_output_shapes	
:�*
dtype0
�
vggish/fc2/weightsVarHandleOp*
_output_shapes
: *#

debug_namevggish/fc2/weights/*
dtype0*
shape:
� �*#
shared_namevggish/fc2/weights
{
&vggish/fc2/weights/Read/ReadVariableOpReadVariableOpvggish/fc2/weights* 
_output_shapes
:
� �*
dtype0
�
vggish/fc1/fc1_2/biasesVarHandleOp*
_output_shapes
: *(

debug_namevggish/fc1/fc1_2/biases/*
dtype0*
shape:� *(
shared_namevggish/fc1/fc1_2/biases
�
+vggish/fc1/fc1_2/biases/Read/ReadVariableOpReadVariableOpvggish/fc1/fc1_2/biases*
_output_shapes	
:� *
dtype0
�
vggish/fc1/fc1_2/weightsVarHandleOp*
_output_shapes
: *)

debug_namevggish/fc1/fc1_2/weights/*
dtype0*
shape:
� � *)
shared_namevggish/fc1/fc1_2/weights
�
,vggish/fc1/fc1_2/weights/Read/ReadVariableOpReadVariableOpvggish/fc1/fc1_2/weights* 
_output_shapes
:
� � *
dtype0
�
vggish/fc1/fc1_1/biasesVarHandleOp*
_output_shapes
: *(

debug_namevggish/fc1/fc1_1/biases/*
dtype0*
shape:� *(
shared_namevggish/fc1/fc1_1/biases
�
+vggish/fc1/fc1_1/biases/Read/ReadVariableOpReadVariableOpvggish/fc1/fc1_1/biases*
_output_shapes	
:� *
dtype0
�
vggish/fc1/fc1_1/weightsVarHandleOp*
_output_shapes
: *)

debug_namevggish/fc1/fc1_1/weights/*
dtype0*
shape:
�`� *)
shared_namevggish/fc1/fc1_1/weights
�
,vggish/fc1/fc1_1/weights/Read/ReadVariableOpReadVariableOpvggish/fc1/fc1_1/weights* 
_output_shapes
:
�`� *
dtype0
�
vggish/conv4/conv4_2/biasesVarHandleOp*
_output_shapes
: *,

debug_namevggish/conv4/conv4_2/biases/*
dtype0*
shape:�*,
shared_namevggish/conv4/conv4_2/biases
�
/vggish/conv4/conv4_2/biases/Read/ReadVariableOpReadVariableOpvggish/conv4/conv4_2/biases*
_output_shapes	
:�*
dtype0
�
vggish/conv4/conv4_2/weightsVarHandleOp*
_output_shapes
: *-

debug_namevggish/conv4/conv4_2/weights/*
dtype0*
shape:��*-
shared_namevggish/conv4/conv4_2/weights
�
0vggish/conv4/conv4_2/weights/Read/ReadVariableOpReadVariableOpvggish/conv4/conv4_2/weights*(
_output_shapes
:��*
dtype0
�
vggish/conv4/conv4_1/biasesVarHandleOp*
_output_shapes
: *,

debug_namevggish/conv4/conv4_1/biases/*
dtype0*
shape:�*,
shared_namevggish/conv4/conv4_1/biases
�
/vggish/conv4/conv4_1/biases/Read/ReadVariableOpReadVariableOpvggish/conv4/conv4_1/biases*
_output_shapes	
:�*
dtype0
�
vggish/conv4/conv4_1/weightsVarHandleOp*
_output_shapes
: *-

debug_namevggish/conv4/conv4_1/weights/*
dtype0*
shape:��*-
shared_namevggish/conv4/conv4_1/weights
�
0vggish/conv4/conv4_1/weights/Read/ReadVariableOpReadVariableOpvggish/conv4/conv4_1/weights*(
_output_shapes
:��*
dtype0
�
vggish/conv3/conv3_2/biasesVarHandleOp*
_output_shapes
: *,

debug_namevggish/conv3/conv3_2/biases/*
dtype0*
shape:�*,
shared_namevggish/conv3/conv3_2/biases
�
/vggish/conv3/conv3_2/biases/Read/ReadVariableOpReadVariableOpvggish/conv3/conv3_2/biases*
_output_shapes	
:�*
dtype0
�
vggish/conv3/conv3_2/weightsVarHandleOp*
_output_shapes
: *-

debug_namevggish/conv3/conv3_2/weights/*
dtype0*
shape:��*-
shared_namevggish/conv3/conv3_2/weights
�
0vggish/conv3/conv3_2/weights/Read/ReadVariableOpReadVariableOpvggish/conv3/conv3_2/weights*(
_output_shapes
:��*
dtype0
�
vggish/conv3/conv3_1/biasesVarHandleOp*
_output_shapes
: *,

debug_namevggish/conv3/conv3_1/biases/*
dtype0*
shape:�*,
shared_namevggish/conv3/conv3_1/biases
�
/vggish/conv3/conv3_1/biases/Read/ReadVariableOpReadVariableOpvggish/conv3/conv3_1/biases*
_output_shapes	
:�*
dtype0
�
vggish/conv3/conv3_1/weightsVarHandleOp*
_output_shapes
: *-

debug_namevggish/conv3/conv3_1/weights/*
dtype0*
shape:��*-
shared_namevggish/conv3/conv3_1/weights
�
0vggish/conv3/conv3_1/weights/Read/ReadVariableOpReadVariableOpvggish/conv3/conv3_1/weights*(
_output_shapes
:��*
dtype0
�
vggish/conv2/biasesVarHandleOp*
_output_shapes
: *$

debug_namevggish/conv2/biases/*
dtype0*
shape:�*$
shared_namevggish/conv2/biases
x
'vggish/conv2/biases/Read/ReadVariableOpReadVariableOpvggish/conv2/biases*
_output_shapes	
:�*
dtype0
�
vggish/conv2/weightsVarHandleOp*
_output_shapes
: *%

debug_namevggish/conv2/weights/*
dtype0*
shape:@�*%
shared_namevggish/conv2/weights
�
(vggish/conv2/weights/Read/ReadVariableOpReadVariableOpvggish/conv2/weights*'
_output_shapes
:@�*
dtype0
�
vggish/conv1/biasesVarHandleOp*
_output_shapes
: *$

debug_namevggish/conv1/biases/*
dtype0*
shape:@*$
shared_namevggish/conv1/biases
w
'vggish/conv1/biases/Read/ReadVariableOpReadVariableOpvggish/conv1/biases*
_output_shapes
:@*
dtype0
�
vggish/conv1/weightsVarHandleOp*
_output_shapes
: *%

debug_namevggish/conv1/weights/*
dtype0*
shape:@*%
shared_namevggish/conv1/weights
�
(vggish/conv1/weights/Read/ReadVariableOpReadVariableOpvggish/conv1/weights*&
_output_shapes
:@*
dtype0
s
serving_default_waveformPlaceholder*#
_output_shapes
:���������*
dtype0*
shape:���������
�
StatefulPartitionedCallStatefulPartitionedCallserving_default_waveformvggish/conv1/weightsvggish/conv1/biasesvggish/conv2/weightsvggish/conv2/biasesvggish/conv3/conv3_1/weightsvggish/conv3/conv3_1/biasesvggish/conv3/conv3_2/weightsvggish/conv3/conv3_2/biasesvggish/conv4/conv4_1/weightsvggish/conv4/conv4_1/biasesvggish/conv4/conv4_2/weightsvggish/conv4/conv4_2/biasesvggish/fc1/fc1_1/weightsvggish/fc1/fc1_1/biasesvggish/fc1/fc1_2/weightsvggish/fc1/fc1_2/biasesvggish/fc2/weightsvggish/fc2/biases*
Tin
2*
Tout
2*
_collective_manager_ids
 *(
_output_shapes
:����������*4
_read_only_resource_inputs
	
*2
config_proto" 

CPU

GPU 2J 8� �J **
f%R#
!__inference_signature_wrapper_797

NoOpNoOp
�
ConstConst"/device:CPU:0*
_output_shapes
: *
dtype0*�
value�B� B�
g

_variables

signatures
#_self_saveable_object_factories
__call__

_vggish_fn*
�
0
1
2
	3

4
5
6
7
8
9
10
11
12
13
14
15
16
17*

serving_default* 
* 

trace_0* 
* 
UO
VARIABLE_VALUEvggish/conv1/weights'_variables/0/.ATTRIBUTES/VARIABLE_VALUE*
TN
VARIABLE_VALUEvggish/conv1/biases'_variables/1/.ATTRIBUTES/VARIABLE_VALUE*
UO
VARIABLE_VALUEvggish/conv2/weights'_variables/2/.ATTRIBUTES/VARIABLE_VALUE*
TN
VARIABLE_VALUEvggish/conv2/biases'_variables/3/.ATTRIBUTES/VARIABLE_VALUE*
]W
VARIABLE_VALUEvggish/conv3/conv3_1/weights'_variables/4/.ATTRIBUTES/VARIABLE_VALUE*
\V
VARIABLE_VALUEvggish/conv3/conv3_1/biases'_variables/5/.ATTRIBUTES/VARIABLE_VALUE*
]W
VARIABLE_VALUEvggish/conv3/conv3_2/weights'_variables/6/.ATTRIBUTES/VARIABLE_VALUE*
\V
VARIABLE_VALUEvggish/conv3/conv3_2/biases'_variables/7/.ATTRIBUTES/VARIABLE_VALUE*
]W
VARIABLE_VALUEvggish/conv4/conv4_1/weights'_variables/8/.ATTRIBUTES/VARIABLE_VALUE*
\V
VARIABLE_VALUEvggish/conv4/conv4_1/biases'_variables/9/.ATTRIBUTES/VARIABLE_VALUE*
^X
VARIABLE_VALUEvggish/conv4/conv4_2/weights(_variables/10/.ATTRIBUTES/VARIABLE_VALUE*
]W
VARIABLE_VALUEvggish/conv4/conv4_2/biases(_variables/11/.ATTRIBUTES/VARIABLE_VALUE*
ZT
VARIABLE_VALUEvggish/fc1/fc1_1/weights(_variables/12/.ATTRIBUTES/VARIABLE_VALUE*
YS
VARIABLE_VALUEvggish/fc1/fc1_1/biases(_variables/13/.ATTRIBUTES/VARIABLE_VALUE*
ZT
VARIABLE_VALUEvggish/fc1/fc1_2/weights(_variables/14/.ATTRIBUTES/VARIABLE_VALUE*
YS
VARIABLE_VALUEvggish/fc1/fc1_2/biases(_variables/15/.ATTRIBUTES/VARIABLE_VALUE*
TN
VARIABLE_VALUEvggish/fc2/weights(_variables/16/.ATTRIBUTES/VARIABLE_VALUE*
SM
VARIABLE_VALUEvggish/fc2/biases(_variables/17/.ATTRIBUTES/VARIABLE_VALUE*
* 
* 
O
saver_filenamePlaceholder*
_output_shapes
: *
dtype0*
shape: 
�
StatefulPartitionedCall_1StatefulPartitionedCallsaver_filenamevggish/conv1/weightsvggish/conv1/biasesvggish/conv2/weightsvggish/conv2/biasesvggish/conv3/conv3_1/weightsvggish/conv3/conv3_1/biasesvggish/conv3/conv3_2/weightsvggish/conv3/conv3_2/biasesvggish/conv4/conv4_1/weightsvggish/conv4/conv4_1/biasesvggish/conv4/conv4_2/weightsvggish/conv4/conv4_2/biasesvggish/fc1/fc1_1/weightsvggish/fc1/fc1_1/biasesvggish/fc1/fc1_2/weightsvggish/fc1/fc1_2/biasesvggish/fc2/weightsvggish/fc2/biasesConst*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes
: * 
_read_only_resource_inputs
 *2
config_proto" 

CPU

GPU 2J 8� �J *%
f R
__inference__traced_save_927
�
StatefulPartitionedCall_2StatefulPartitionedCallsaver_filenamevggish/conv1/weightsvggish/conv1/biasesvggish/conv2/weightsvggish/conv2/biasesvggish/conv3/conv3_1/weightsvggish/conv3/conv3_1/biasesvggish/conv3/conv3_2/weightsvggish/conv3/conv3_2/biasesvggish/conv4/conv4_1/weightsvggish/conv4/conv4_1/biasesvggish/conv4/conv4_2/weightsvggish/conv4/conv4_2/biasesvggish/fc1/fc1_1/weightsvggish/fc1/fc1_1/biasesvggish/fc1/fc1_2/weightsvggish/fc1/fc1_2/biasesvggish/fc2/weightsvggish/fc2/biases*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes
: * 
_read_only_resource_inputs
 *2
config_proto" 

CPU

GPU 2J 8� �J *(
f#R!
__inference__traced_restore_990��
�
�
!__inference_signature_wrapper_797
waveform!
unknown:@
	unknown_0:@$
	unknown_1:@�
	unknown_2:	�%
	unknown_3:��
	unknown_4:	�%
	unknown_5:��
	unknown_6:	�%
	unknown_7:��
	unknown_8:	�%
	unknown_9:��

unknown_10:	�

unknown_11:
�`� 

unknown_12:	� 

unknown_13:
� � 

unknown_14:	� 

unknown_15:
� �

unknown_16:	�
identity��StatefulPartitionedCall�
StatefulPartitionedCallStatefulPartitionedCallwaveformunknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4	unknown_5	unknown_6	unknown_7	unknown_8	unknown_9
unknown_10
unknown_11
unknown_12
unknown_13
unknown_14
unknown_15
unknown_16*
Tin
2*
Tout
2*
_collective_manager_ids
 *(
_output_shapes
:����������*4
_read_only_resource_inputs
	
*2
config_proto" 

CPU

GPU 2J 8� �J */
f*R(
&__inference_restored_function_body_755p
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*(
_output_shapes
:����������<
NoOpNoOp^StatefulPartitionedCall*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*F
_input_shapes5
3:���������: : : : : : : : : : : : : : : : : : 22
StatefulPartitionedCallStatefulPartitionedCall:#

_user_specified_name793:#

_user_specified_name791:#

_user_specified_name789:#

_user_specified_name787:#

_user_specified_name785:#

_user_specified_name783:#

_user_specified_name781:#

_user_specified_name779:#


_user_specified_name777:#	

_user_specified_name775:#

_user_specified_name773:#

_user_specified_name771:#

_user_specified_name769:#

_user_specified_name767:#

_user_specified_name765:#

_user_specified_name763:#

_user_specified_name761:#

_user_specified_name759:M I
#
_output_shapes
:���������
"
_user_specified_name
waveform
��
�

 __inference_wrapped_function_480
placeholderE
+vggish_conv1_conv2d_readvariableop_resource:@:
,vggish_conv1_biasadd_readvariableop_resource:@F
+vggish_conv2_conv2d_readvariableop_resource:@�;
,vggish_conv2_biasadd_readvariableop_resource:	�O
3vggish_conv3_conv3_1_conv2d_readvariableop_resource:��C
4vggish_conv3_conv3_1_biasadd_readvariableop_resource:	�O
3vggish_conv3_conv3_2_conv2d_readvariableop_resource:��C
4vggish_conv3_conv3_2_biasadd_readvariableop_resource:	�O
3vggish_conv4_conv4_1_conv2d_readvariableop_resource:��C
4vggish_conv4_conv4_1_biasadd_readvariableop_resource:	�O
3vggish_conv4_conv4_2_conv2d_readvariableop_resource:��C
4vggish_conv4_conv4_2_biasadd_readvariableop_resource:	�C
/vggish_fc1_fc1_1_matmul_readvariableop_resource:
�`� ?
0vggish_fc1_fc1_1_biasadd_readvariableop_resource:	� C
/vggish_fc1_fc1_2_matmul_readvariableop_resource:
� � ?
0vggish_fc1_fc1_2_biasadd_readvariableop_resource:	� =
)vggish_fc2_matmul_readvariableop_resource:
� �9
*vggish_fc2_biasadd_readvariableop_resource:	�
vggish_embedding��
"log_mel_features/stft/frame_lengthConst*
_output_shapes
: *
dtype0*
value
B :�2$
"log_mel_features/stft/frame_length�
 log_mel_features/stft/frame_stepConst*
_output_shapes
: *
dtype0*
value
B :�2"
 log_mel_features/stft/frame_step�
 log_mel_features/stft/fft_lengthConst*
_output_shapes
: *
dtype0*
value
B :�2"
 log_mel_features/stft/fft_length�
 log_mel_features/stft/frame/axisConst*
_output_shapes
: *
dtype0*
valueB :
���������2"
 log_mel_features/stft/frame/axis�
!log_mel_features/stft/frame/ShapeShapeplaceholder*
T0*
_output_shapes
:2#
!log_mel_features/stft/frame/Shape:���
 log_mel_features/stft/frame/RankConst*
_output_shapes
: *
dtype0*
value	B :2"
 log_mel_features/stft/frame/Rank�
'log_mel_features/stft/frame/range/startConst*
_output_shapes
: *
dtype0*
value	B : 2)
'log_mel_features/stft/frame/range/start�
'log_mel_features/stft/frame/range/deltaConst*
_output_shapes
: *
dtype0*
value	B :2)
'log_mel_features/stft/frame/range/delta�
!log_mel_features/stft/frame/rangeRange0log_mel_features/stft/frame/range/start:output:0)log_mel_features/stft/frame/Rank:output:00log_mel_features/stft/frame/range/delta:output:0*
_output_shapes
:2#
!log_mel_features/stft/frame/range�
/log_mel_features/stft/frame/strided_slice/stackConst*
_output_shapes
:*
dtype0*
valueB:
���������21
/log_mel_features/stft/frame/strided_slice/stack�
1log_mel_features/stft/frame/strided_slice/stack_1Const*
_output_shapes
:*
dtype0*
valueB: 23
1log_mel_features/stft/frame/strided_slice/stack_1�
1log_mel_features/stft/frame/strided_slice/stack_2Const*
_output_shapes
:*
dtype0*
valueB:23
1log_mel_features/stft/frame/strided_slice/stack_2�
)log_mel_features/stft/frame/strided_sliceStridedSlice*log_mel_features/stft/frame/range:output:08log_mel_features/stft/frame/strided_slice/stack:output:0:log_mel_features/stft/frame/strided_slice/stack_1:output:0:log_mel_features/stft/frame/strided_slice/stack_2:output:0*
Index0*
T0*
_output_shapes
: *
shrink_axis_mask2+
)log_mel_features/stft/frame/strided_slice�
!log_mel_features/stft/frame/sub/yConst*
_output_shapes
: *
dtype0*
value	B :2#
!log_mel_features/stft/frame/sub/y�
log_mel_features/stft/frame/subSub)log_mel_features/stft/frame/Rank:output:0*log_mel_features/stft/frame/sub/y:output:0*
T0*
_output_shapes
: 2!
log_mel_features/stft/frame/sub�
!log_mel_features/stft/frame/sub_1Sub#log_mel_features/stft/frame/sub:z:02log_mel_features/stft/frame/strided_slice:output:0*
T0*
_output_shapes
: 2#
!log_mel_features/stft/frame/sub_1�
$log_mel_features/stft/frame/packed/1Const*
_output_shapes
: *
dtype0*
value	B :2&
$log_mel_features/stft/frame/packed/1�
"log_mel_features/stft/frame/packedPack2log_mel_features/stft/frame/strided_slice:output:0-log_mel_features/stft/frame/packed/1:output:0%log_mel_features/stft/frame/sub_1:z:0*
N*
T0*
_output_shapes
:2$
"log_mel_features/stft/frame/packed�
+log_mel_features/stft/frame/split/split_dimConst*
_output_shapes
: *
dtype0*
value	B : 2-
+log_mel_features/stft/frame/split/split_dim�
!log_mel_features/stft/frame/splitSplitV*log_mel_features/stft/frame/Shape:output:0+log_mel_features/stft/frame/packed:output:04log_mel_features/stft/frame/split/split_dim:output:0*

Tlen0*
T0*"
_output_shapes
: :: *
	num_split2#
!log_mel_features/stft/frame/split�
)log_mel_features/stft/frame/Reshape/shapeConst*
_output_shapes
: *
dtype0*
valueB 2+
)log_mel_features/stft/frame/Reshape/shape�
#log_mel_features/stft/frame/ReshapeReshape*log_mel_features/stft/frame/split:output:12log_mel_features/stft/frame/Reshape/shape:output:0*
T0*
_output_shapes
: 2%
#log_mel_features/stft/frame/Reshape�
 log_mel_features/stft/frame/SizeConst*
_output_shapes
: *
dtype0*
value	B : 2"
 log_mel_features/stft/frame/Size�
"log_mel_features/stft/frame/Size_1Const*
_output_shapes
: *
dtype0*
value	B : 2$
"log_mel_features/stft/frame/Size_1�
!log_mel_features/stft/frame/sub_2Sub,log_mel_features/stft/frame/Reshape:output:0+log_mel_features/stft/frame_length:output:0*
T0*
_output_shapes
: 2#
!log_mel_features/stft/frame/sub_2�
$log_mel_features/stft/frame/floordivFloorDiv%log_mel_features/stft/frame/sub_2:z:0)log_mel_features/stft/frame_step:output:0*
T0*
_output_shapes
: 2&
$log_mel_features/stft/frame/floordiv�
!log_mel_features/stft/frame/add/xConst*
_output_shapes
: *
dtype0*
value	B :2#
!log_mel_features/stft/frame/add/x�
log_mel_features/stft/frame/addAddV2*log_mel_features/stft/frame/add/x:output:0(log_mel_features/stft/frame/floordiv:z:0*
T0*
_output_shapes
: 2!
log_mel_features/stft/frame/add�
%log_mel_features/stft/frame/Maximum/xConst*
_output_shapes
: *
dtype0*
value	B : 2'
%log_mel_features/stft/frame/Maximum/x�
#log_mel_features/stft/frame/MaximumMaximum.log_mel_features/stft/frame/Maximum/x:output:0#log_mel_features/stft/frame/add:z:0*
T0*
_output_shapes
: 2%
#log_mel_features/stft/frame/Maximum�
%log_mel_features/stft/frame/gcd/ConstConst*
_output_shapes
: *
dtype0*
value	B :P2'
%log_mel_features/stft/frame/gcd/Const�
(log_mel_features/stft/frame/floordiv_1/yConst*
_output_shapes
: *
dtype0*
value	B :P2*
(log_mel_features/stft/frame/floordiv_1/y�
&log_mel_features/stft/frame/floordiv_1FloorDiv+log_mel_features/stft/frame_length:output:01log_mel_features/stft/frame/floordiv_1/y:output:0*
T0*
_output_shapes
: 2(
&log_mel_features/stft/frame/floordiv_1�
(log_mel_features/stft/frame/floordiv_2/yConst*
_output_shapes
: *
dtype0*
value	B :P2*
(log_mel_features/stft/frame/floordiv_2/y�
&log_mel_features/stft/frame/floordiv_2FloorDiv)log_mel_features/stft/frame_step:output:01log_mel_features/stft/frame/floordiv_2/y:output:0*
T0*
_output_shapes
: 2(
&log_mel_features/stft/frame/floordiv_2�
(log_mel_features/stft/frame/floordiv_3/yConst*
_output_shapes
: *
dtype0*
value	B :P2*
(log_mel_features/stft/frame/floordiv_3/y�
&log_mel_features/stft/frame/floordiv_3FloorDiv,log_mel_features/stft/frame/Reshape:output:01log_mel_features/stft/frame/floordiv_3/y:output:0*
T0*
_output_shapes
: 2(
&log_mel_features/stft/frame/floordiv_3�
!log_mel_features/stft/frame/mul/yConst*
_output_shapes
: *
dtype0*
value	B :P2#
!log_mel_features/stft/frame/mul/y�
log_mel_features/stft/frame/mulMul*log_mel_features/stft/frame/floordiv_3:z:0*log_mel_features/stft/frame/mul/y:output:0*
T0*
_output_shapes
: 2!
log_mel_features/stft/frame/mul�
+log_mel_features/stft/frame/concat/values_1Pack#log_mel_features/stft/frame/mul:z:0*
N*
T0*
_output_shapes
:2-
+log_mel_features/stft/frame/concat/values_1�
'log_mel_features/stft/frame/concat/axisConst*
_output_shapes
: *
dtype0*
value	B : 2)
'log_mel_features/stft/frame/concat/axis�
"log_mel_features/stft/frame/concatConcatV2*log_mel_features/stft/frame/split:output:04log_mel_features/stft/frame/concat/values_1:output:0*log_mel_features/stft/frame/split:output:20log_mel_features/stft/frame/concat/axis:output:0*
N*
T0*
_output_shapes
:2$
"log_mel_features/stft/frame/concat�
/log_mel_features/stft/frame/concat_1/values_1/1Const*
_output_shapes
: *
dtype0*
value	B :P21
/log_mel_features/stft/frame/concat_1/values_1/1�
-log_mel_features/stft/frame/concat_1/values_1Pack*log_mel_features/stft/frame/floordiv_3:z:08log_mel_features/stft/frame/concat_1/values_1/1:output:0*
N*
T0*
_output_shapes
:2/
-log_mel_features/stft/frame/concat_1/values_1�
)log_mel_features/stft/frame/concat_1/axisConst*
_output_shapes
: *
dtype0*
value	B : 2+
)log_mel_features/stft/frame/concat_1/axis�
$log_mel_features/stft/frame/concat_1ConcatV2*log_mel_features/stft/frame/split:output:06log_mel_features/stft/frame/concat_1/values_1:output:0*log_mel_features/stft/frame/split:output:22log_mel_features/stft/frame/concat_1/axis:output:0*
N*
T0*
_output_shapes
:2&
$log_mel_features/stft/frame/concat_1�
&log_mel_features/stft/frame/zeros_likeConst*
_output_shapes
:*
dtype0*
valueB: 2(
&log_mel_features/stft/frame/zeros_like�
+log_mel_features/stft/frame/ones_like/ShapeConst*
_output_shapes
:*
dtype0*
valueB:2-
+log_mel_features/stft/frame/ones_like/Shape�
+log_mel_features/stft/frame/ones_like/ConstConst*
_output_shapes
: *
dtype0*
value	B :2-
+log_mel_features/stft/frame/ones_like/Const�
%log_mel_features/stft/frame/ones_likeFill4log_mel_features/stft/frame/ones_like/Shape:output:04log_mel_features/stft/frame/ones_like/Const:output:0*
T0*
_output_shapes
:2'
%log_mel_features/stft/frame/ones_like�
(log_mel_features/stft/frame/StridedSliceStridedSliceplaceholder/log_mel_features/stft/frame/zeros_like:output:0+log_mel_features/stft/frame/concat:output:0.log_mel_features/stft/frame/ones_like:output:0*
Index0*
T0*#
_output_shapes
:���������2*
(log_mel_features/stft/frame/StridedSlice�
%log_mel_features/stft/frame/Reshape_1Reshape1log_mel_features/stft/frame/StridedSlice:output:0-log_mel_features/stft/frame/concat_1:output:0*
T0*'
_output_shapes
:���������P2'
%log_mel_features/stft/frame/Reshape_1�
)log_mel_features/stft/frame/range_1/startConst*
_output_shapes
: *
dtype0*
value	B : 2+
)log_mel_features/stft/frame/range_1/start�
)log_mel_features/stft/frame/range_1/deltaConst*
_output_shapes
: *
dtype0*
value	B :2+
)log_mel_features/stft/frame/range_1/delta�
#log_mel_features/stft/frame/range_1Range2log_mel_features/stft/frame/range_1/start:output:0'log_mel_features/stft/frame/Maximum:z:02log_mel_features/stft/frame/range_1/delta:output:0*#
_output_shapes
:���������2%
#log_mel_features/stft/frame/range_1�
!log_mel_features/stft/frame/mul_1Mul,log_mel_features/stft/frame/range_1:output:0*log_mel_features/stft/frame/floordiv_2:z:0*
T0*#
_output_shapes
:���������2#
!log_mel_features/stft/frame/mul_1�
-log_mel_features/stft/frame/Reshape_2/shape/1Const*
_output_shapes
: *
dtype0*
value	B :2/
-log_mel_features/stft/frame/Reshape_2/shape/1�
+log_mel_features/stft/frame/Reshape_2/shapePack'log_mel_features/stft/frame/Maximum:z:06log_mel_features/stft/frame/Reshape_2/shape/1:output:0*
N*
T0*
_output_shapes
:2-
+log_mel_features/stft/frame/Reshape_2/shape�
%log_mel_features/stft/frame/Reshape_2Reshape%log_mel_features/stft/frame/mul_1:z:04log_mel_features/stft/frame/Reshape_2/shape:output:0*
T0*'
_output_shapes
:���������2'
%log_mel_features/stft/frame/Reshape_2�
)log_mel_features/stft/frame/range_2/startConst*
_output_shapes
: *
dtype0*
value	B : 2+
)log_mel_features/stft/frame/range_2/start�
)log_mel_features/stft/frame/range_2/deltaConst*
_output_shapes
: *
dtype0*
value	B :2+
)log_mel_features/stft/frame/range_2/delta�
#log_mel_features/stft/frame/range_2Range2log_mel_features/stft/frame/range_2/start:output:0*log_mel_features/stft/frame/floordiv_1:z:02log_mel_features/stft/frame/range_2/delta:output:0*
_output_shapes
:2%
#log_mel_features/stft/frame/range_2�
-log_mel_features/stft/frame/Reshape_3/shape/0Const*
_output_shapes
: *
dtype0*
value	B :2/
-log_mel_features/stft/frame/Reshape_3/shape/0�
+log_mel_features/stft/frame/Reshape_3/shapePack6log_mel_features/stft/frame/Reshape_3/shape/0:output:0*log_mel_features/stft/frame/floordiv_1:z:0*
N*
T0*
_output_shapes
:2-
+log_mel_features/stft/frame/Reshape_3/shape�
%log_mel_features/stft/frame/Reshape_3Reshape,log_mel_features/stft/frame/range_2:output:04log_mel_features/stft/frame/Reshape_3/shape:output:0*
T0*
_output_shapes

:2'
%log_mel_features/stft/frame/Reshape_3�
!log_mel_features/stft/frame/add_1AddV2.log_mel_features/stft/frame/Reshape_2:output:0.log_mel_features/stft/frame/Reshape_3:output:0*
T0*'
_output_shapes
:���������2#
!log_mel_features/stft/frame/add_1�
$log_mel_features/stft/frame/GatherV2GatherV2.log_mel_features/stft/frame/Reshape_1:output:0%log_mel_features/stft/frame/add_1:z:02log_mel_features/stft/frame/strided_slice:output:0*
Taxis0*
Tindices0*
Tparams0*+
_output_shapes
:���������P2&
$log_mel_features/stft/frame/GatherV2�
-log_mel_features/stft/frame/concat_2/values_1Pack'log_mel_features/stft/frame/Maximum:z:0+log_mel_features/stft/frame_length:output:0*
N*
T0*
_output_shapes
:2/
-log_mel_features/stft/frame/concat_2/values_1�
)log_mel_features/stft/frame/concat_2/axisConst*
_output_shapes
: *
dtype0*
value	B : 2+
)log_mel_features/stft/frame/concat_2/axis�
$log_mel_features/stft/frame/concat_2ConcatV2*log_mel_features/stft/frame/split:output:06log_mel_features/stft/frame/concat_2/values_1:output:0*log_mel_features/stft/frame/split:output:22log_mel_features/stft/frame/concat_2/axis:output:0*
N*
T0*
_output_shapes
:2&
$log_mel_features/stft/frame/concat_2�
%log_mel_features/stft/frame/Reshape_4Reshape-log_mel_features/stft/frame/GatherV2:output:0-log_mel_features/stft/frame/concat_2:output:0*
T0*(
_output_shapes
:����������2'
%log_mel_features/stft/frame/Reshape_4�
*log_mel_features/stft/hann_window/periodicConst*
_output_shapes
: *
dtype0
*
value	B
 Z2,
*log_mel_features/stft/hann_window/periodic�
&log_mel_features/stft/hann_window/CastCast3log_mel_features/stft/hann_window/periodic:output:0*

DstT0*

SrcT0
*
_output_shapes
: 2(
&log_mel_features/stft/hann_window/Cast�
,log_mel_features/stft/hann_window/FloorMod/yConst*
_output_shapes
: *
dtype0*
value	B :2.
,log_mel_features/stft/hann_window/FloorMod/y�
*log_mel_features/stft/hann_window/FloorModFloorMod+log_mel_features/stft/frame_length:output:05log_mel_features/stft/hann_window/FloorMod/y:output:0*
T0*
_output_shapes
: 2,
*log_mel_features/stft/hann_window/FloorMod�
'log_mel_features/stft/hann_window/sub/xConst*
_output_shapes
: *
dtype0*
value	B :2)
'log_mel_features/stft/hann_window/sub/x�
%log_mel_features/stft/hann_window/subSub0log_mel_features/stft/hann_window/sub/x:output:0.log_mel_features/stft/hann_window/FloorMod:z:0*
T0*
_output_shapes
: 2'
%log_mel_features/stft/hann_window/sub�
%log_mel_features/stft/hann_window/mulMul*log_mel_features/stft/hann_window/Cast:y:0)log_mel_features/stft/hann_window/sub:z:0*
T0*
_output_shapes
: 2'
%log_mel_features/stft/hann_window/mul�
%log_mel_features/stft/hann_window/addAddV2+log_mel_features/stft/frame_length:output:0)log_mel_features/stft/hann_window/mul:z:0*
T0*
_output_shapes
: 2'
%log_mel_features/stft/hann_window/add�
)log_mel_features/stft/hann_window/sub_1/yConst*
_output_shapes
: *
dtype0*
value	B :2+
)log_mel_features/stft/hann_window/sub_1/y�
'log_mel_features/stft/hann_window/sub_1Sub)log_mel_features/stft/hann_window/add:z:02log_mel_features/stft/hann_window/sub_1/y:output:0*
T0*
_output_shapes
: 2)
'log_mel_features/stft/hann_window/sub_1�
(log_mel_features/stft/hann_window/Cast_1Cast+log_mel_features/stft/hann_window/sub_1:z:0*

DstT0*

SrcT0*
_output_shapes
: 2*
(log_mel_features/stft/hann_window/Cast_1�
-log_mel_features/stft/hann_window/range/startConst*
_output_shapes
: *
dtype0*
value	B : 2/
-log_mel_features/stft/hann_window/range/start�
-log_mel_features/stft/hann_window/range/deltaConst*
_output_shapes
: *
dtype0*
value	B :2/
-log_mel_features/stft/hann_window/range/delta�
'log_mel_features/stft/hann_window/rangeRange6log_mel_features/stft/hann_window/range/start:output:0+log_mel_features/stft/frame_length:output:06log_mel_features/stft/hann_window/range/delta:output:0*
_output_shapes	
:�2)
'log_mel_features/stft/hann_window/range�
(log_mel_features/stft/hann_window/Cast_2Cast0log_mel_features/stft/hann_window/range:output:0*

DstT0*

SrcT0*
_output_shapes	
:�2*
(log_mel_features/stft/hann_window/Cast_2�
'log_mel_features/stft/hann_window/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *��@2)
'log_mel_features/stft/hann_window/Const�
'log_mel_features/stft/hann_window/mul_1Mul0log_mel_features/stft/hann_window/Const:output:0,log_mel_features/stft/hann_window/Cast_2:y:0*
T0*
_output_shapes	
:�2)
'log_mel_features/stft/hann_window/mul_1�
)log_mel_features/stft/hann_window/truedivRealDiv+log_mel_features/stft/hann_window/mul_1:z:0,log_mel_features/stft/hann_window/Cast_1:y:0*
T0*
_output_shapes	
:�2+
)log_mel_features/stft/hann_window/truediv�
%log_mel_features/stft/hann_window/CosCos-log_mel_features/stft/hann_window/truediv:z:0*
T0*
_output_shapes	
:�2'
%log_mel_features/stft/hann_window/Cos�
)log_mel_features/stft/hann_window/mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *   ?2+
)log_mel_features/stft/hann_window/mul_2/x�
'log_mel_features/stft/hann_window/mul_2Mul2log_mel_features/stft/hann_window/mul_2/x:output:0)log_mel_features/stft/hann_window/Cos:y:0*
T0*
_output_shapes	
:�2)
'log_mel_features/stft/hann_window/mul_2�
)log_mel_features/stft/hann_window/sub_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *   ?2+
)log_mel_features/stft/hann_window/sub_2/x�
'log_mel_features/stft/hann_window/sub_2Sub2log_mel_features/stft/hann_window/sub_2/x:output:0+log_mel_features/stft/hann_window/mul_2:z:0*
T0*
_output_shapes	
:�2)
'log_mel_features/stft/hann_window/sub_2�
log_mel_features/stft/mulMul.log_mel_features/stft/frame/Reshape_4:output:0+log_mel_features/stft/hann_window/sub_2:z:0*
T0*(
_output_shapes
:����������2
log_mel_features/stft/mul�
!log_mel_features/stft/rfft/packedPack)log_mel_features/stft/fft_length:output:0*
N*
T0*
_output_shapes
:2#
!log_mel_features/stft/rfft/packed�
'log_mel_features/stft/rfft/Pad/paddingsConst*
_output_shapes

:*
dtype0*)
value B"            p   2)
'log_mel_features/stft/rfft/Pad/paddings�
log_mel_features/stft/rfft/PadPadlog_mel_features/stft/mul:z:00log_mel_features/stft/rfft/Pad/paddings:output:0*
T0*(
_output_shapes
:����������2 
log_mel_features/stft/rfft/Pad�
%log_mel_features/stft/rfft/fft_lengthConst*
_output_shapes
:*
dtype0*
valueB:�2'
%log_mel_features/stft/rfft/fft_length�
log_mel_features/stft/rfftRFFT'log_mel_features/stft/rfft/Pad:output:0.log_mel_features/stft/rfft/fft_length:output:0*(
_output_shapes
:����������2
log_mel_features/stft/rfft�
log_mel_features/Abs
ComplexAbs#log_mel_features/stft/rfft:output:0*(
_output_shapes
:����������2
log_mel_features/Abs�
:log_mel_features/linear_to_mel_weight_matrix/sample_rate/xConst*
_output_shapes
: *
dtype0*
value
B :�}2<
:log_mel_features/linear_to_mel_weight_matrix/sample_rate/x�
8log_mel_features/linear_to_mel_weight_matrix/sample_rateCastClog_mel_features/linear_to_mel_weight_matrix/sample_rate/x:output:0*

DstT0*

SrcT0*
_output_shapes
: 2:
8log_mel_features/linear_to_mel_weight_matrix/sample_rate�
=log_mel_features/linear_to_mel_weight_matrix/lower_edge_hertzConst*
_output_shapes
: *
dtype0*
valueB
 *  �B2?
=log_mel_features/linear_to_mel_weight_matrix/lower_edge_hertz�
=log_mel_features/linear_to_mel_weight_matrix/upper_edge_hertzConst*
_output_shapes
: *
dtype0*
valueB
 * `�E2?
=log_mel_features/linear_to_mel_weight_matrix/upper_edge_hertz�
2log_mel_features/linear_to_mel_weight_matrix/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *    24
2log_mel_features/linear_to_mel_weight_matrix/Const�
6log_mel_features/linear_to_mel_weight_matrix/truediv/yConst*
_output_shapes
: *
dtype0*
valueB
 *   @28
6log_mel_features/linear_to_mel_weight_matrix/truediv/y�
4log_mel_features/linear_to_mel_weight_matrix/truedivRealDiv<log_mel_features/linear_to_mel_weight_matrix/sample_rate:y:0?log_mel_features/linear_to_mel_weight_matrix/truediv/y:output:0*
T0*
_output_shapes
: 26
4log_mel_features/linear_to_mel_weight_matrix/truediv�
9log_mel_features/linear_to_mel_weight_matrix/linspace/numConst*
_output_shapes
: *
dtype0*
value
B :�2;
9log_mel_features/linear_to_mel_weight_matrix/linspace/num�
:log_mel_features/linear_to_mel_weight_matrix/linspace/CastCastBlog_mel_features/linear_to_mel_weight_matrix/linspace/num:output:0*

DstT0*

SrcT0*
_output_shapes
: 2<
:log_mel_features/linear_to_mel_weight_matrix/linspace/Cast�
<log_mel_features/linear_to_mel_weight_matrix/linspace/Cast_1Cast>log_mel_features/linear_to_mel_weight_matrix/linspace/Cast:y:0*

DstT0*

SrcT0*
_output_shapes
: 2>
<log_mel_features/linear_to_mel_weight_matrix/linspace/Cast_1�
;log_mel_features/linear_to_mel_weight_matrix/linspace/ShapeConst*
_output_shapes
: *
dtype0*
valueB 2=
;log_mel_features/linear_to_mel_weight_matrix/linspace/Shape�
=log_mel_features/linear_to_mel_weight_matrix/linspace/Shape_1Const*
_output_shapes
: *
dtype0*
valueB 2?
=log_mel_features/linear_to_mel_weight_matrix/linspace/Shape_1�
Clog_mel_features/linear_to_mel_weight_matrix/linspace/BroadcastArgsBroadcastArgsDlog_mel_features/linear_to_mel_weight_matrix/linspace/Shape:output:0Flog_mel_features/linear_to_mel_weight_matrix/linspace/Shape_1:output:0*
_output_shapes
: 2E
Clog_mel_features/linear_to_mel_weight_matrix/linspace/BroadcastArgs�
Alog_mel_features/linear_to_mel_weight_matrix/linspace/BroadcastToBroadcastTo;log_mel_features/linear_to_mel_weight_matrix/Const:output:0Hlog_mel_features/linear_to_mel_weight_matrix/linspace/BroadcastArgs:r0:0*
T0*
_output_shapes
: 2C
Alog_mel_features/linear_to_mel_weight_matrix/linspace/BroadcastTo�
Clog_mel_features/linear_to_mel_weight_matrix/linspace/BroadcastTo_1BroadcastTo8log_mel_features/linear_to_mel_weight_matrix/truediv:z:0Hlog_mel_features/linear_to_mel_weight_matrix/linspace/BroadcastArgs:r0:0*
T0*
_output_shapes
: 2E
Clog_mel_features/linear_to_mel_weight_matrix/linspace/BroadcastTo_1�
Dlog_mel_features/linear_to_mel_weight_matrix/linspace/ExpandDims/dimConst*
_output_shapes
: *
dtype0*
value	B : 2F
Dlog_mel_features/linear_to_mel_weight_matrix/linspace/ExpandDims/dim�
@log_mel_features/linear_to_mel_weight_matrix/linspace/ExpandDims
ExpandDimsJlog_mel_features/linear_to_mel_weight_matrix/linspace/BroadcastTo:output:0Mlog_mel_features/linear_to_mel_weight_matrix/linspace/ExpandDims/dim:output:0*
T0*
_output_shapes
:2B
@log_mel_features/linear_to_mel_weight_matrix/linspace/ExpandDims�
Flog_mel_features/linear_to_mel_weight_matrix/linspace/ExpandDims_1/dimConst*
_output_shapes
: *
dtype0*
value	B : 2H
Flog_mel_features/linear_to_mel_weight_matrix/linspace/ExpandDims_1/dim�
Blog_mel_features/linear_to_mel_weight_matrix/linspace/ExpandDims_1
ExpandDimsLlog_mel_features/linear_to_mel_weight_matrix/linspace/BroadcastTo_1:output:0Olog_mel_features/linear_to_mel_weight_matrix/linspace/ExpandDims_1/dim:output:0*
T0*
_output_shapes
:2D
Blog_mel_features/linear_to_mel_weight_matrix/linspace/ExpandDims_1�
=log_mel_features/linear_to_mel_weight_matrix/linspace/Shape_2Const*
_output_shapes
:*
dtype0*
valueB:2?
=log_mel_features/linear_to_mel_weight_matrix/linspace/Shape_2�
=log_mel_features/linear_to_mel_weight_matrix/linspace/Shape_3Const*
_output_shapes
:*
dtype0*
valueB:2?
=log_mel_features/linear_to_mel_weight_matrix/linspace/Shape_3�
Ilog_mel_features/linear_to_mel_weight_matrix/linspace/strided_slice/stackConst*
_output_shapes
:*
dtype0*
valueB: 2K
Ilog_mel_features/linear_to_mel_weight_matrix/linspace/strided_slice/stack�
Klog_mel_features/linear_to_mel_weight_matrix/linspace/strided_slice/stack_1Const*
_output_shapes
:*
dtype0*
valueB:2M
Klog_mel_features/linear_to_mel_weight_matrix/linspace/strided_slice/stack_1�
Klog_mel_features/linear_to_mel_weight_matrix/linspace/strided_slice/stack_2Const*
_output_shapes
:*
dtype0*
valueB:2M
Klog_mel_features/linear_to_mel_weight_matrix/linspace/strided_slice/stack_2�
Clog_mel_features/linear_to_mel_weight_matrix/linspace/strided_sliceStridedSliceFlog_mel_features/linear_to_mel_weight_matrix/linspace/Shape_3:output:0Rlog_mel_features/linear_to_mel_weight_matrix/linspace/strided_slice/stack:output:0Tlog_mel_features/linear_to_mel_weight_matrix/linspace/strided_slice/stack_1:output:0Tlog_mel_features/linear_to_mel_weight_matrix/linspace/strided_slice/stack_2:output:0*
Index0*
T0*
_output_shapes
: *
shrink_axis_mask2E
Clog_mel_features/linear_to_mel_weight_matrix/linspace/strided_slice�
;log_mel_features/linear_to_mel_weight_matrix/linspace/add/yConst*
_output_shapes
: *
dtype0*
value	B : 2=
;log_mel_features/linear_to_mel_weight_matrix/linspace/add/y�
9log_mel_features/linear_to_mel_weight_matrix/linspace/addAddV2Llog_mel_features/linear_to_mel_weight_matrix/linspace/strided_slice:output:0Dlog_mel_features/linear_to_mel_weight_matrix/linspace/add/y:output:0*
T0*
_output_shapes
: 2;
9log_mel_features/linear_to_mel_weight_matrix/linspace/add�
Hlog_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2/conditionConst*
_output_shapes
: *
dtype0
*
value	B
 Z2J
Hlog_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2/condition�
@log_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2/tConst*
_output_shapes
: *
dtype0*
value	B : 2B
@log_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2/t�
>log_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2SelectV2Qlog_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2/condition:output:0Ilog_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2/t:output:0=log_mel_features/linear_to_mel_weight_matrix/linspace/add:z:0*
T0*
_output_shapes
: 2@
>log_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2�
;log_mel_features/linear_to_mel_weight_matrix/linspace/sub/yConst*
_output_shapes
: *
dtype0*
value	B :2=
;log_mel_features/linear_to_mel_weight_matrix/linspace/sub/y�
9log_mel_features/linear_to_mel_weight_matrix/linspace/subSub>log_mel_features/linear_to_mel_weight_matrix/linspace/Cast:y:0Dlog_mel_features/linear_to_mel_weight_matrix/linspace/sub/y:output:0*
T0*
_output_shapes
: 2;
9log_mel_features/linear_to_mel_weight_matrix/linspace/sub�
?log_mel_features/linear_to_mel_weight_matrix/linspace/Maximum/yConst*
_output_shapes
: *
dtype0*
value	B : 2A
?log_mel_features/linear_to_mel_weight_matrix/linspace/Maximum/y�
=log_mel_features/linear_to_mel_weight_matrix/linspace/MaximumMaximum=log_mel_features/linear_to_mel_weight_matrix/linspace/sub:z:0Hlog_mel_features/linear_to_mel_weight_matrix/linspace/Maximum/y:output:0*
T0*
_output_shapes
: 2?
=log_mel_features/linear_to_mel_weight_matrix/linspace/Maximum�
=log_mel_features/linear_to_mel_weight_matrix/linspace/sub_1/yConst*
_output_shapes
: *
dtype0*
value	B :2?
=log_mel_features/linear_to_mel_weight_matrix/linspace/sub_1/y�
;log_mel_features/linear_to_mel_weight_matrix/linspace/sub_1Sub>log_mel_features/linear_to_mel_weight_matrix/linspace/Cast:y:0Flog_mel_features/linear_to_mel_weight_matrix/linspace/sub_1/y:output:0*
T0*
_output_shapes
: 2=
;log_mel_features/linear_to_mel_weight_matrix/linspace/sub_1�
Alog_mel_features/linear_to_mel_weight_matrix/linspace/Maximum_1/yConst*
_output_shapes
: *
dtype0*
value	B :2C
Alog_mel_features/linear_to_mel_weight_matrix/linspace/Maximum_1/y�
?log_mel_features/linear_to_mel_weight_matrix/linspace/Maximum_1Maximum?log_mel_features/linear_to_mel_weight_matrix/linspace/sub_1:z:0Jlog_mel_features/linear_to_mel_weight_matrix/linspace/Maximum_1/y:output:0*
T0*
_output_shapes
: 2A
?log_mel_features/linear_to_mel_weight_matrix/linspace/Maximum_1�
;log_mel_features/linear_to_mel_weight_matrix/linspace/sub_2SubKlog_mel_features/linear_to_mel_weight_matrix/linspace/ExpandDims_1:output:0Ilog_mel_features/linear_to_mel_weight_matrix/linspace/ExpandDims:output:0*
T0*
_output_shapes
:2=
;log_mel_features/linear_to_mel_weight_matrix/linspace/sub_2�
<log_mel_features/linear_to_mel_weight_matrix/linspace/Cast_2CastClog_mel_features/linear_to_mel_weight_matrix/linspace/Maximum_1:z:0*

DstT0*

SrcT0*
_output_shapes
: 2>
<log_mel_features/linear_to_mel_weight_matrix/linspace/Cast_2�
=log_mel_features/linear_to_mel_weight_matrix/linspace/truedivRealDiv?log_mel_features/linear_to_mel_weight_matrix/linspace/sub_2:z:0@log_mel_features/linear_to_mel_weight_matrix/linspace/Cast_2:y:0*
T0*
_output_shapes
:2?
=log_mel_features/linear_to_mel_weight_matrix/linspace/truediv�
Dlog_mel_features/linear_to_mel_weight_matrix/linspace/GreaterEqual/yConst*
_output_shapes
: *
dtype0*
value	B : 2F
Dlog_mel_features/linear_to_mel_weight_matrix/linspace/GreaterEqual/y�
Blog_mel_features/linear_to_mel_weight_matrix/linspace/GreaterEqualGreaterEqual>log_mel_features/linear_to_mel_weight_matrix/linspace/Cast:y:0Mlog_mel_features/linear_to_mel_weight_matrix/linspace/GreaterEqual/y:output:0*
T0*
_output_shapes
: 2D
Blog_mel_features/linear_to_mel_weight_matrix/linspace/GreaterEqual�
Blog_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2_1/eConst*
_output_shapes
: *
dtype0*
valueB :
���������2D
Blog_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2_1/e�
@log_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2_1SelectV2Flog_mel_features/linear_to_mel_weight_matrix/linspace/GreaterEqual:z:0Clog_mel_features/linear_to_mel_weight_matrix/linspace/Maximum_1:z:0Klog_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2_1/e:output:0*
T0*
_output_shapes
: 2B
@log_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2_1�
Alog_mel_features/linear_to_mel_weight_matrix/linspace/range/startConst*
_output_shapes
: *
dtype0	*
value	B	 R2C
Alog_mel_features/linear_to_mel_weight_matrix/linspace/range/start�
Alog_mel_features/linear_to_mel_weight_matrix/linspace/range/deltaConst*
_output_shapes
: *
dtype0	*
value	B	 R2C
Alog_mel_features/linear_to_mel_weight_matrix/linspace/range/delta�
@log_mel_features/linear_to_mel_weight_matrix/linspace/range/CastCastIlog_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2_1:output:0*

DstT0	*

SrcT0*
_output_shapes
: 2B
@log_mel_features/linear_to_mel_weight_matrix/linspace/range/Cast�
;log_mel_features/linear_to_mel_weight_matrix/linspace/rangeRangeJlog_mel_features/linear_to_mel_weight_matrix/linspace/range/start:output:0Dlog_mel_features/linear_to_mel_weight_matrix/linspace/range/Cast:y:0Jlog_mel_features/linear_to_mel_weight_matrix/linspace/range/delta:output:0*

Tidx0	*
_output_shapes	
:�2=
;log_mel_features/linear_to_mel_weight_matrix/linspace/range�
<log_mel_features/linear_to_mel_weight_matrix/linspace/Cast_3CastDlog_mel_features/linear_to_mel_weight_matrix/linspace/range:output:0*

DstT0*

SrcT0	*
_output_shapes	
:�2>
<log_mel_features/linear_to_mel_weight_matrix/linspace/Cast_3�
Clog_mel_features/linear_to_mel_weight_matrix/linspace/range_1/startConst*
_output_shapes
: *
dtype0*
value	B : 2E
Clog_mel_features/linear_to_mel_weight_matrix/linspace/range_1/start�
Clog_mel_features/linear_to_mel_weight_matrix/linspace/range_1/deltaConst*
_output_shapes
: *
dtype0*
value	B :2E
Clog_mel_features/linear_to_mel_weight_matrix/linspace/range_1/delta�
=log_mel_features/linear_to_mel_weight_matrix/linspace/range_1RangeLlog_mel_features/linear_to_mel_weight_matrix/linspace/range_1/start:output:0Llog_mel_features/linear_to_mel_weight_matrix/linspace/strided_slice:output:0Llog_mel_features/linear_to_mel_weight_matrix/linspace/range_1/delta:output:0*
_output_shapes
:2?
=log_mel_features/linear_to_mel_weight_matrix/linspace/range_1�
;log_mel_features/linear_to_mel_weight_matrix/linspace/EqualEqualGlog_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2:output:0Flog_mel_features/linear_to_mel_weight_matrix/linspace/range_1:output:0*
T0*
_output_shapes
:2=
;log_mel_features/linear_to_mel_weight_matrix/linspace/Equal�
Blog_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2_2/eConst*
_output_shapes
: *
dtype0*
value	B :2D
Blog_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2_2/e�
@log_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2_2SelectV2?log_mel_features/linear_to_mel_weight_matrix/linspace/Equal:z:0Alog_mel_features/linear_to_mel_weight_matrix/linspace/Maximum:z:0Klog_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2_2/e:output:0*
T0*
_output_shapes
:2B
@log_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2_2�
=log_mel_features/linear_to_mel_weight_matrix/linspace/ReshapeReshape@log_mel_features/linear_to_mel_weight_matrix/linspace/Cast_3:y:0Ilog_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2_2:output:0*
T0*
_output_shapes	
:�2?
=log_mel_features/linear_to_mel_weight_matrix/linspace/Reshape�
9log_mel_features/linear_to_mel_weight_matrix/linspace/mulMulAlog_mel_features/linear_to_mel_weight_matrix/linspace/truediv:z:0Flog_mel_features/linear_to_mel_weight_matrix/linspace/Reshape:output:0*
T0*
_output_shapes	
:�2;
9log_mel_features/linear_to_mel_weight_matrix/linspace/mul�
;log_mel_features/linear_to_mel_weight_matrix/linspace/add_1AddV2Ilog_mel_features/linear_to_mel_weight_matrix/linspace/ExpandDims:output:0=log_mel_features/linear_to_mel_weight_matrix/linspace/mul:z:0*
T0*
_output_shapes	
:�2=
;log_mel_features/linear_to_mel_weight_matrix/linspace/add_1�
<log_mel_features/linear_to_mel_weight_matrix/linspace/concatConcatV2Ilog_mel_features/linear_to_mel_weight_matrix/linspace/ExpandDims:output:0?log_mel_features/linear_to_mel_weight_matrix/linspace/add_1:z:0Klog_mel_features/linear_to_mel_weight_matrix/linspace/ExpandDims_1:output:0Glog_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2:output:0*
N*
T0*
_output_shapes	
:�2>
<log_mel_features/linear_to_mel_weight_matrix/linspace/concat�
@log_mel_features/linear_to_mel_weight_matrix/linspace/zeros_likeConst*
_output_shapes
:*
dtype0*
valueB: 2B
@log_mel_features/linear_to_mel_weight_matrix/linspace/zeros_like�
@log_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2_3SelectV2?log_mel_features/linear_to_mel_weight_matrix/linspace/Equal:z:0>log_mel_features/linear_to_mel_weight_matrix/linspace/Cast:y:0Flog_mel_features/linear_to_mel_weight_matrix/linspace/Shape_2:output:0*
T0*
_output_shapes
:2B
@log_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2_3�
;log_mel_features/linear_to_mel_weight_matrix/linspace/SliceSliceElog_mel_features/linear_to_mel_weight_matrix/linspace/concat:output:0Ilog_mel_features/linear_to_mel_weight_matrix/linspace/zeros_like:output:0Ilog_mel_features/linear_to_mel_weight_matrix/linspace/SelectV2_3:output:0*
Index0*
T0*
_output_shapes	
:�2=
;log_mel_features/linear_to_mel_weight_matrix/linspace/Slice�
@log_mel_features/linear_to_mel_weight_matrix/strided_slice/stackConst*
_output_shapes
:*
dtype0*
valueB:2B
@log_mel_features/linear_to_mel_weight_matrix/strided_slice/stack�
Blog_mel_features/linear_to_mel_weight_matrix/strided_slice/stack_1Const*
_output_shapes
:*
dtype0*
valueB: 2D
Blog_mel_features/linear_to_mel_weight_matrix/strided_slice/stack_1�
Blog_mel_features/linear_to_mel_weight_matrix/strided_slice/stack_2Const*
_output_shapes
:*
dtype0*
valueB:2D
Blog_mel_features/linear_to_mel_weight_matrix/strided_slice/stack_2�
:log_mel_features/linear_to_mel_weight_matrix/strided_sliceStridedSliceDlog_mel_features/linear_to_mel_weight_matrix/linspace/Slice:output:0Ilog_mel_features/linear_to_mel_weight_matrix/strided_slice/stack:output:0Klog_mel_features/linear_to_mel_weight_matrix/strided_slice/stack_1:output:0Klog_mel_features/linear_to_mel_weight_matrix/strided_slice/stack_2:output:0*
Index0*
T0*
_output_shapes	
:�*
end_mask2<
:log_mel_features/linear_to_mel_weight_matrix/strided_slice�
Clog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/truediv/yConst*
_output_shapes
: *
dtype0*
valueB
 *  /D2E
Clog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/truediv/y�
Alog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/truedivRealDivClog_mel_features/linear_to_mel_weight_matrix/strided_slice:output:0Llog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/truediv/y:output:0*
T0*
_output_shapes	
:�2C
Alog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/truediv�
?log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/add/xConst*
_output_shapes
: *
dtype0*
valueB
 *  �?2A
?log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/add/x�
=log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/addAddV2Hlog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/add/x:output:0Elog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/truediv:z:0*
T0*
_output_shapes	
:�2?
=log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/add�
=log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/LogLogAlog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/add:z:0*
T0*
_output_shapes	
:�2?
=log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/Log�
?log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 * ��D2A
?log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/mul/x�
=log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/mulMulHlog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/mul/x:output:0Alog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/Log:y:0*
T0*
_output_shapes	
:�2?
=log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/mul�
;log_mel_features/linear_to_mel_weight_matrix/ExpandDims/dimConst*
_output_shapes
: *
dtype0*
value	B :2=
;log_mel_features/linear_to_mel_weight_matrix/ExpandDims/dim�
7log_mel_features/linear_to_mel_weight_matrix/ExpandDims
ExpandDimsAlog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel/mul:z:0Dlog_mel_features/linear_to_mel_weight_matrix/ExpandDims/dim:output:0*
T0*
_output_shapes
:	�29
7log_mel_features/linear_to_mel_weight_matrix/ExpandDims�
Elog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/truediv/yConst*
_output_shapes
: *
dtype0*
valueB
 *  /D2G
Elog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/truediv/y�
Clog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/truedivRealDivFlog_mel_features/linear_to_mel_weight_matrix/lower_edge_hertz:output:0Nlog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/truediv/y:output:0*
T0*
_output_shapes
: 2E
Clog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/truediv�
Alog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/add/xConst*
_output_shapes
: *
dtype0*
valueB
 *  �?2C
Alog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/add/x�
?log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/addAddV2Jlog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/add/x:output:0Glog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/truediv:z:0*
T0*
_output_shapes
: 2A
?log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/add�
?log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/LogLogClog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/add:z:0*
T0*
_output_shapes
: 2A
?log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/Log�
Alog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 * ��D2C
Alog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/mul/x�
?log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/mulMulJlog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/mul/x:output:0Clog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/Log:y:0*
T0*
_output_shapes
: 2A
?log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/mul�
Elog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/truediv/yConst*
_output_shapes
: *
dtype0*
valueB
 *  /D2G
Elog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/truediv/y�
Clog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/truedivRealDivFlog_mel_features/linear_to_mel_weight_matrix/upper_edge_hertz:output:0Nlog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/truediv/y:output:0*
T0*
_output_shapes
: 2E
Clog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/truediv�
Alog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/add/xConst*
_output_shapes
: *
dtype0*
valueB
 *  �?2C
Alog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/add/x�
?log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/addAddV2Jlog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/add/x:output:0Glog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/truediv:z:0*
T0*
_output_shapes
: 2A
?log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/add�
?log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/LogLogClog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/add:z:0*
T0*
_output_shapes
: 2A
?log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/Log�
Alog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 * ��D2C
Alog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/mul/x�
?log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/mulMulJlog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/mul/x:output:0Clog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/Log:y:0*
T0*
_output_shapes
: 2A
?log_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/mul�
;log_mel_features/linear_to_mel_weight_matrix/linspace_1/numConst*
_output_shapes
: *
dtype0*
value	B :B2=
;log_mel_features/linear_to_mel_weight_matrix/linspace_1/num�
<log_mel_features/linear_to_mel_weight_matrix/linspace_1/CastCastDlog_mel_features/linear_to_mel_weight_matrix/linspace_1/num:output:0*

DstT0*

SrcT0*
_output_shapes
: 2>
<log_mel_features/linear_to_mel_weight_matrix/linspace_1/Cast�
>log_mel_features/linear_to_mel_weight_matrix/linspace_1/Cast_1Cast@log_mel_features/linear_to_mel_weight_matrix/linspace_1/Cast:y:0*

DstT0*

SrcT0*
_output_shapes
: 2@
>log_mel_features/linear_to_mel_weight_matrix/linspace_1/Cast_1�
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/ShapeConst*
_output_shapes
: *
dtype0*
valueB 2?
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/Shape�
?log_mel_features/linear_to_mel_weight_matrix/linspace_1/Shape_1Const*
_output_shapes
: *
dtype0*
valueB 2A
?log_mel_features/linear_to_mel_weight_matrix/linspace_1/Shape_1�
Elog_mel_features/linear_to_mel_weight_matrix/linspace_1/BroadcastArgsBroadcastArgsFlog_mel_features/linear_to_mel_weight_matrix/linspace_1/Shape:output:0Hlog_mel_features/linear_to_mel_weight_matrix/linspace_1/Shape_1:output:0*
_output_shapes
: 2G
Elog_mel_features/linear_to_mel_weight_matrix/linspace_1/BroadcastArgs�
Clog_mel_features/linear_to_mel_weight_matrix/linspace_1/BroadcastToBroadcastToClog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_1/mul:z:0Jlog_mel_features/linear_to_mel_weight_matrix/linspace_1/BroadcastArgs:r0:0*
T0*
_output_shapes
: 2E
Clog_mel_features/linear_to_mel_weight_matrix/linspace_1/BroadcastTo�
Elog_mel_features/linear_to_mel_weight_matrix/linspace_1/BroadcastTo_1BroadcastToClog_mel_features/linear_to_mel_weight_matrix/hertz_to_mel_2/mul:z:0Jlog_mel_features/linear_to_mel_weight_matrix/linspace_1/BroadcastArgs:r0:0*
T0*
_output_shapes
: 2G
Elog_mel_features/linear_to_mel_weight_matrix/linspace_1/BroadcastTo_1�
Flog_mel_features/linear_to_mel_weight_matrix/linspace_1/ExpandDims/dimConst*
_output_shapes
: *
dtype0*
value	B : 2H
Flog_mel_features/linear_to_mel_weight_matrix/linspace_1/ExpandDims/dim�
Blog_mel_features/linear_to_mel_weight_matrix/linspace_1/ExpandDims
ExpandDimsLlog_mel_features/linear_to_mel_weight_matrix/linspace_1/BroadcastTo:output:0Olog_mel_features/linear_to_mel_weight_matrix/linspace_1/ExpandDims/dim:output:0*
T0*
_output_shapes
:2D
Blog_mel_features/linear_to_mel_weight_matrix/linspace_1/ExpandDims�
Hlog_mel_features/linear_to_mel_weight_matrix/linspace_1/ExpandDims_1/dimConst*
_output_shapes
: *
dtype0*
value	B : 2J
Hlog_mel_features/linear_to_mel_weight_matrix/linspace_1/ExpandDims_1/dim�
Dlog_mel_features/linear_to_mel_weight_matrix/linspace_1/ExpandDims_1
ExpandDimsNlog_mel_features/linear_to_mel_weight_matrix/linspace_1/BroadcastTo_1:output:0Qlog_mel_features/linear_to_mel_weight_matrix/linspace_1/ExpandDims_1/dim:output:0*
T0*
_output_shapes
:2F
Dlog_mel_features/linear_to_mel_weight_matrix/linspace_1/ExpandDims_1�
?log_mel_features/linear_to_mel_weight_matrix/linspace_1/Shape_2Const*
_output_shapes
:*
dtype0*
valueB:2A
?log_mel_features/linear_to_mel_weight_matrix/linspace_1/Shape_2�
?log_mel_features/linear_to_mel_weight_matrix/linspace_1/Shape_3Const*
_output_shapes
:*
dtype0*
valueB:2A
?log_mel_features/linear_to_mel_weight_matrix/linspace_1/Shape_3�
Klog_mel_features/linear_to_mel_weight_matrix/linspace_1/strided_slice/stackConst*
_output_shapes
:*
dtype0*
valueB: 2M
Klog_mel_features/linear_to_mel_weight_matrix/linspace_1/strided_slice/stack�
Mlog_mel_features/linear_to_mel_weight_matrix/linspace_1/strided_slice/stack_1Const*
_output_shapes
:*
dtype0*
valueB:2O
Mlog_mel_features/linear_to_mel_weight_matrix/linspace_1/strided_slice/stack_1�
Mlog_mel_features/linear_to_mel_weight_matrix/linspace_1/strided_slice/stack_2Const*
_output_shapes
:*
dtype0*
valueB:2O
Mlog_mel_features/linear_to_mel_weight_matrix/linspace_1/strided_slice/stack_2�
Elog_mel_features/linear_to_mel_weight_matrix/linspace_1/strided_sliceStridedSliceHlog_mel_features/linear_to_mel_weight_matrix/linspace_1/Shape_3:output:0Tlog_mel_features/linear_to_mel_weight_matrix/linspace_1/strided_slice/stack:output:0Vlog_mel_features/linear_to_mel_weight_matrix/linspace_1/strided_slice/stack_1:output:0Vlog_mel_features/linear_to_mel_weight_matrix/linspace_1/strided_slice/stack_2:output:0*
Index0*
T0*
_output_shapes
: *
shrink_axis_mask2G
Elog_mel_features/linear_to_mel_weight_matrix/linspace_1/strided_slice�
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/add/yConst*
_output_shapes
: *
dtype0*
value	B : 2?
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/add/y�
;log_mel_features/linear_to_mel_weight_matrix/linspace_1/addAddV2Nlog_mel_features/linear_to_mel_weight_matrix/linspace_1/strided_slice:output:0Flog_mel_features/linear_to_mel_weight_matrix/linspace_1/add/y:output:0*
T0*
_output_shapes
: 2=
;log_mel_features/linear_to_mel_weight_matrix/linspace_1/add�
Jlog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2/conditionConst*
_output_shapes
: *
dtype0
*
value	B
 Z2L
Jlog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2/condition�
Blog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2/tConst*
_output_shapes
: *
dtype0*
value	B : 2D
Blog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2/t�
@log_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2SelectV2Slog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2/condition:output:0Klog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2/t:output:0?log_mel_features/linear_to_mel_weight_matrix/linspace_1/add:z:0*
T0*
_output_shapes
: 2B
@log_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2�
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/sub/yConst*
_output_shapes
: *
dtype0*
value	B :2?
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/sub/y�
;log_mel_features/linear_to_mel_weight_matrix/linspace_1/subSub@log_mel_features/linear_to_mel_weight_matrix/linspace_1/Cast:y:0Flog_mel_features/linear_to_mel_weight_matrix/linspace_1/sub/y:output:0*
T0*
_output_shapes
: 2=
;log_mel_features/linear_to_mel_weight_matrix/linspace_1/sub�
Alog_mel_features/linear_to_mel_weight_matrix/linspace_1/Maximum/yConst*
_output_shapes
: *
dtype0*
value	B : 2C
Alog_mel_features/linear_to_mel_weight_matrix/linspace_1/Maximum/y�
?log_mel_features/linear_to_mel_weight_matrix/linspace_1/MaximumMaximum?log_mel_features/linear_to_mel_weight_matrix/linspace_1/sub:z:0Jlog_mel_features/linear_to_mel_weight_matrix/linspace_1/Maximum/y:output:0*
T0*
_output_shapes
: 2A
?log_mel_features/linear_to_mel_weight_matrix/linspace_1/Maximum�
?log_mel_features/linear_to_mel_weight_matrix/linspace_1/sub_1/yConst*
_output_shapes
: *
dtype0*
value	B :2A
?log_mel_features/linear_to_mel_weight_matrix/linspace_1/sub_1/y�
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/sub_1Sub@log_mel_features/linear_to_mel_weight_matrix/linspace_1/Cast:y:0Hlog_mel_features/linear_to_mel_weight_matrix/linspace_1/sub_1/y:output:0*
T0*
_output_shapes
: 2?
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/sub_1�
Clog_mel_features/linear_to_mel_weight_matrix/linspace_1/Maximum_1/yConst*
_output_shapes
: *
dtype0*
value	B :2E
Clog_mel_features/linear_to_mel_weight_matrix/linspace_1/Maximum_1/y�
Alog_mel_features/linear_to_mel_weight_matrix/linspace_1/Maximum_1MaximumAlog_mel_features/linear_to_mel_weight_matrix/linspace_1/sub_1:z:0Llog_mel_features/linear_to_mel_weight_matrix/linspace_1/Maximum_1/y:output:0*
T0*
_output_shapes
: 2C
Alog_mel_features/linear_to_mel_weight_matrix/linspace_1/Maximum_1�
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/sub_2SubMlog_mel_features/linear_to_mel_weight_matrix/linspace_1/ExpandDims_1:output:0Klog_mel_features/linear_to_mel_weight_matrix/linspace_1/ExpandDims:output:0*
T0*
_output_shapes
:2?
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/sub_2�
>log_mel_features/linear_to_mel_weight_matrix/linspace_1/Cast_2CastElog_mel_features/linear_to_mel_weight_matrix/linspace_1/Maximum_1:z:0*

DstT0*

SrcT0*
_output_shapes
: 2@
>log_mel_features/linear_to_mel_weight_matrix/linspace_1/Cast_2�
?log_mel_features/linear_to_mel_weight_matrix/linspace_1/truedivRealDivAlog_mel_features/linear_to_mel_weight_matrix/linspace_1/sub_2:z:0Blog_mel_features/linear_to_mel_weight_matrix/linspace_1/Cast_2:y:0*
T0*
_output_shapes
:2A
?log_mel_features/linear_to_mel_weight_matrix/linspace_1/truediv�
Flog_mel_features/linear_to_mel_weight_matrix/linspace_1/GreaterEqual/yConst*
_output_shapes
: *
dtype0*
value	B : 2H
Flog_mel_features/linear_to_mel_weight_matrix/linspace_1/GreaterEqual/y�
Dlog_mel_features/linear_to_mel_weight_matrix/linspace_1/GreaterEqualGreaterEqual@log_mel_features/linear_to_mel_weight_matrix/linspace_1/Cast:y:0Olog_mel_features/linear_to_mel_weight_matrix/linspace_1/GreaterEqual/y:output:0*
T0*
_output_shapes
: 2F
Dlog_mel_features/linear_to_mel_weight_matrix/linspace_1/GreaterEqual�
Dlog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2_1/eConst*
_output_shapes
: *
dtype0*
valueB :
���������2F
Dlog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2_1/e�
Blog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2_1SelectV2Hlog_mel_features/linear_to_mel_weight_matrix/linspace_1/GreaterEqual:z:0Elog_mel_features/linear_to_mel_weight_matrix/linspace_1/Maximum_1:z:0Mlog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2_1/e:output:0*
T0*
_output_shapes
: 2D
Blog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2_1�
Clog_mel_features/linear_to_mel_weight_matrix/linspace_1/range/startConst*
_output_shapes
: *
dtype0	*
value	B	 R2E
Clog_mel_features/linear_to_mel_weight_matrix/linspace_1/range/start�
Clog_mel_features/linear_to_mel_weight_matrix/linspace_1/range/deltaConst*
_output_shapes
: *
dtype0	*
value	B	 R2E
Clog_mel_features/linear_to_mel_weight_matrix/linspace_1/range/delta�
Blog_mel_features/linear_to_mel_weight_matrix/linspace_1/range/CastCastKlog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2_1:output:0*

DstT0	*

SrcT0*
_output_shapes
: 2D
Blog_mel_features/linear_to_mel_weight_matrix/linspace_1/range/Cast�
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/rangeRangeLlog_mel_features/linear_to_mel_weight_matrix/linspace_1/range/start:output:0Flog_mel_features/linear_to_mel_weight_matrix/linspace_1/range/Cast:y:0Llog_mel_features/linear_to_mel_weight_matrix/linspace_1/range/delta:output:0*

Tidx0	*
_output_shapes
:@2?
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/range�
>log_mel_features/linear_to_mel_weight_matrix/linspace_1/Cast_3CastFlog_mel_features/linear_to_mel_weight_matrix/linspace_1/range:output:0*

DstT0*

SrcT0	*
_output_shapes
:@2@
>log_mel_features/linear_to_mel_weight_matrix/linspace_1/Cast_3�
Elog_mel_features/linear_to_mel_weight_matrix/linspace_1/range_1/startConst*
_output_shapes
: *
dtype0*
value	B : 2G
Elog_mel_features/linear_to_mel_weight_matrix/linspace_1/range_1/start�
Elog_mel_features/linear_to_mel_weight_matrix/linspace_1/range_1/deltaConst*
_output_shapes
: *
dtype0*
value	B :2G
Elog_mel_features/linear_to_mel_weight_matrix/linspace_1/range_1/delta�
?log_mel_features/linear_to_mel_weight_matrix/linspace_1/range_1RangeNlog_mel_features/linear_to_mel_weight_matrix/linspace_1/range_1/start:output:0Nlog_mel_features/linear_to_mel_weight_matrix/linspace_1/strided_slice:output:0Nlog_mel_features/linear_to_mel_weight_matrix/linspace_1/range_1/delta:output:0*
_output_shapes
:2A
?log_mel_features/linear_to_mel_weight_matrix/linspace_1/range_1�
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/EqualEqualIlog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2:output:0Hlog_mel_features/linear_to_mel_weight_matrix/linspace_1/range_1:output:0*
T0*
_output_shapes
:2?
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/Equal�
Dlog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2_2/eConst*
_output_shapes
: *
dtype0*
value	B :2F
Dlog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2_2/e�
Blog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2_2SelectV2Alog_mel_features/linear_to_mel_weight_matrix/linspace_1/Equal:z:0Clog_mel_features/linear_to_mel_weight_matrix/linspace_1/Maximum:z:0Mlog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2_2/e:output:0*
T0*
_output_shapes
:2D
Blog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2_2�
?log_mel_features/linear_to_mel_weight_matrix/linspace_1/ReshapeReshapeBlog_mel_features/linear_to_mel_weight_matrix/linspace_1/Cast_3:y:0Klog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2_2:output:0*
T0*
_output_shapes
:@2A
?log_mel_features/linear_to_mel_weight_matrix/linspace_1/Reshape�
;log_mel_features/linear_to_mel_weight_matrix/linspace_1/mulMulClog_mel_features/linear_to_mel_weight_matrix/linspace_1/truediv:z:0Hlog_mel_features/linear_to_mel_weight_matrix/linspace_1/Reshape:output:0*
T0*
_output_shapes
:@2=
;log_mel_features/linear_to_mel_weight_matrix/linspace_1/mul�
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/add_1AddV2Klog_mel_features/linear_to_mel_weight_matrix/linspace_1/ExpandDims:output:0?log_mel_features/linear_to_mel_weight_matrix/linspace_1/mul:z:0*
T0*
_output_shapes
:@2?
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/add_1�
>log_mel_features/linear_to_mel_weight_matrix/linspace_1/concatConcatV2Klog_mel_features/linear_to_mel_weight_matrix/linspace_1/ExpandDims:output:0Alog_mel_features/linear_to_mel_weight_matrix/linspace_1/add_1:z:0Mlog_mel_features/linear_to_mel_weight_matrix/linspace_1/ExpandDims_1:output:0Ilog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2:output:0*
N*
T0*
_output_shapes
:B2@
>log_mel_features/linear_to_mel_weight_matrix/linspace_1/concat�
Blog_mel_features/linear_to_mel_weight_matrix/linspace_1/zeros_likeConst*
_output_shapes
:*
dtype0*
valueB: 2D
Blog_mel_features/linear_to_mel_weight_matrix/linspace_1/zeros_like�
Blog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2_3SelectV2Alog_mel_features/linear_to_mel_weight_matrix/linspace_1/Equal:z:0@log_mel_features/linear_to_mel_weight_matrix/linspace_1/Cast:y:0Hlog_mel_features/linear_to_mel_weight_matrix/linspace_1/Shape_2:output:0*
T0*
_output_shapes
:2D
Blog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2_3�
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/SliceSliceGlog_mel_features/linear_to_mel_weight_matrix/linspace_1/concat:output:0Klog_mel_features/linear_to_mel_weight_matrix/linspace_1/zeros_like:output:0Klog_mel_features/linear_to_mel_weight_matrix/linspace_1/SelectV2_3:output:0*
Index0*
T0*
_output_shapes
:B2?
=log_mel_features/linear_to_mel_weight_matrix/linspace_1/Slice�
?log_mel_features/linear_to_mel_weight_matrix/frame/frame_lengthConst*
_output_shapes
: *
dtype0*
value	B :2A
?log_mel_features/linear_to_mel_weight_matrix/frame/frame_length�
=log_mel_features/linear_to_mel_weight_matrix/frame/frame_stepConst*
_output_shapes
: *
dtype0*
value	B :2?
=log_mel_features/linear_to_mel_weight_matrix/frame/frame_step�
7log_mel_features/linear_to_mel_weight_matrix/frame/axisConst*
_output_shapes
: *
dtype0*
valueB :
���������29
7log_mel_features/linear_to_mel_weight_matrix/frame/axis�
8log_mel_features/linear_to_mel_weight_matrix/frame/ShapeConst*
_output_shapes
:*
dtype0*
valueB:B2:
8log_mel_features/linear_to_mel_weight_matrix/frame/Shape�
=log_mel_features/linear_to_mel_weight_matrix/frame/Size/ConstConst*
_output_shapes
: *
dtype0*
valueB 2?
=log_mel_features/linear_to_mel_weight_matrix/frame/Size/Const�
7log_mel_features/linear_to_mel_weight_matrix/frame/SizeConst*
_output_shapes
: *
dtype0*
value	B : 29
7log_mel_features/linear_to_mel_weight_matrix/frame/Size�
?log_mel_features/linear_to_mel_weight_matrix/frame/Size_1/ConstConst*
_output_shapes
: *
dtype0*
valueB 2A
?log_mel_features/linear_to_mel_weight_matrix/frame/Size_1/Const�
9log_mel_features/linear_to_mel_weight_matrix/frame/Size_1Const*
_output_shapes
: *
dtype0*
value	B : 2;
9log_mel_features/linear_to_mel_weight_matrix/frame/Size_1�
8log_mel_features/linear_to_mel_weight_matrix/frame/sub/xConst*
_output_shapes
: *
dtype0*
value	B :B2:
8log_mel_features/linear_to_mel_weight_matrix/frame/sub/x�
6log_mel_features/linear_to_mel_weight_matrix/frame/subSubAlog_mel_features/linear_to_mel_weight_matrix/frame/sub/x:output:0Hlog_mel_features/linear_to_mel_weight_matrix/frame/frame_length:output:0*
T0*
_output_shapes
: 28
6log_mel_features/linear_to_mel_weight_matrix/frame/sub�
;log_mel_features/linear_to_mel_weight_matrix/frame/floordivFloorDiv:log_mel_features/linear_to_mel_weight_matrix/frame/sub:z:0Flog_mel_features/linear_to_mel_weight_matrix/frame/frame_step:output:0*
T0*
_output_shapes
: 2=
;log_mel_features/linear_to_mel_weight_matrix/frame/floordiv�
8log_mel_features/linear_to_mel_weight_matrix/frame/add/xConst*
_output_shapes
: *
dtype0*
value	B :2:
8log_mel_features/linear_to_mel_weight_matrix/frame/add/x�
6log_mel_features/linear_to_mel_weight_matrix/frame/addAddV2Alog_mel_features/linear_to_mel_weight_matrix/frame/add/x:output:0?log_mel_features/linear_to_mel_weight_matrix/frame/floordiv:z:0*
T0*
_output_shapes
: 28
6log_mel_features/linear_to_mel_weight_matrix/frame/add�
<log_mel_features/linear_to_mel_weight_matrix/frame/Maximum/xConst*
_output_shapes
: *
dtype0*
value	B : 2>
<log_mel_features/linear_to_mel_weight_matrix/frame/Maximum/x�
:log_mel_features/linear_to_mel_weight_matrix/frame/MaximumMaximumElog_mel_features/linear_to_mel_weight_matrix/frame/Maximum/x:output:0:log_mel_features/linear_to_mel_weight_matrix/frame/add:z:0*
T0*
_output_shapes
: 2<
:log_mel_features/linear_to_mel_weight_matrix/frame/Maximum�
<log_mel_features/linear_to_mel_weight_matrix/frame/gcd/ConstConst*
_output_shapes
: *
dtype0*
value	B :2>
<log_mel_features/linear_to_mel_weight_matrix/frame/gcd/Const�
?log_mel_features/linear_to_mel_weight_matrix/frame/floordiv_1/yConst*
_output_shapes
: *
dtype0*
value	B :2A
?log_mel_features/linear_to_mel_weight_matrix/frame/floordiv_1/y�
=log_mel_features/linear_to_mel_weight_matrix/frame/floordiv_1FloorDivHlog_mel_features/linear_to_mel_weight_matrix/frame/frame_length:output:0Hlog_mel_features/linear_to_mel_weight_matrix/frame/floordiv_1/y:output:0*
T0*
_output_shapes
: 2?
=log_mel_features/linear_to_mel_weight_matrix/frame/floordiv_1�
?log_mel_features/linear_to_mel_weight_matrix/frame/floordiv_2/yConst*
_output_shapes
: *
dtype0*
value	B :2A
?log_mel_features/linear_to_mel_weight_matrix/frame/floordiv_2/y�
=log_mel_features/linear_to_mel_weight_matrix/frame/floordiv_2FloorDivFlog_mel_features/linear_to_mel_weight_matrix/frame/frame_step:output:0Hlog_mel_features/linear_to_mel_weight_matrix/frame/floordiv_2/y:output:0*
T0*
_output_shapes
: 2?
=log_mel_features/linear_to_mel_weight_matrix/frame/floordiv_2�
Blog_mel_features/linear_to_mel_weight_matrix/frame/concat/values_0Const*
_output_shapes
: *
dtype0*
valueB 2D
Blog_mel_features/linear_to_mel_weight_matrix/frame/concat/values_0�
Blog_mel_features/linear_to_mel_weight_matrix/frame/concat/values_1Const*
_output_shapes
:*
dtype0*
valueB:B2D
Blog_mel_features/linear_to_mel_weight_matrix/frame/concat/values_1�
Blog_mel_features/linear_to_mel_weight_matrix/frame/concat/values_2Const*
_output_shapes
: *
dtype0*
valueB 2D
Blog_mel_features/linear_to_mel_weight_matrix/frame/concat/values_2�
>log_mel_features/linear_to_mel_weight_matrix/frame/concat/axisConst*
_output_shapes
: *
dtype0*
value	B : 2@
>log_mel_features/linear_to_mel_weight_matrix/frame/concat/axis�
9log_mel_features/linear_to_mel_weight_matrix/frame/concatConcatV2Klog_mel_features/linear_to_mel_weight_matrix/frame/concat/values_0:output:0Klog_mel_features/linear_to_mel_weight_matrix/frame/concat/values_1:output:0Klog_mel_features/linear_to_mel_weight_matrix/frame/concat/values_2:output:0Glog_mel_features/linear_to_mel_weight_matrix/frame/concat/axis:output:0*
N*
T0*
_output_shapes
:2;
9log_mel_features/linear_to_mel_weight_matrix/frame/concat�
Dlog_mel_features/linear_to_mel_weight_matrix/frame/concat_1/values_0Const*
_output_shapes
: *
dtype0*
valueB 2F
Dlog_mel_features/linear_to_mel_weight_matrix/frame/concat_1/values_0�
Dlog_mel_features/linear_to_mel_weight_matrix/frame/concat_1/values_1Const*
_output_shapes
:*
dtype0*
valueB"B      2F
Dlog_mel_features/linear_to_mel_weight_matrix/frame/concat_1/values_1�
Dlog_mel_features/linear_to_mel_weight_matrix/frame/concat_1/values_2Const*
_output_shapes
: *
dtype0*
valueB 2F
Dlog_mel_features/linear_to_mel_weight_matrix/frame/concat_1/values_2�
@log_mel_features/linear_to_mel_weight_matrix/frame/concat_1/axisConst*
_output_shapes
: *
dtype0*
value	B : 2B
@log_mel_features/linear_to_mel_weight_matrix/frame/concat_1/axis�
;log_mel_features/linear_to_mel_weight_matrix/frame/concat_1ConcatV2Mlog_mel_features/linear_to_mel_weight_matrix/frame/concat_1/values_0:output:0Mlog_mel_features/linear_to_mel_weight_matrix/frame/concat_1/values_1:output:0Mlog_mel_features/linear_to_mel_weight_matrix/frame/concat_1/values_2:output:0Ilog_mel_features/linear_to_mel_weight_matrix/frame/concat_1/axis:output:0*
N*
T0*
_output_shapes
:2=
;log_mel_features/linear_to_mel_weight_matrix/frame/concat_1�
Dlog_mel_features/linear_to_mel_weight_matrix/frame/zeros_like/tensorConst*
_output_shapes
:*
dtype0*
valueB:B2F
Dlog_mel_features/linear_to_mel_weight_matrix/frame/zeros_like/tensor�
=log_mel_features/linear_to_mel_weight_matrix/frame/zeros_likeConst*
_output_shapes
:*
dtype0*
valueB: 2?
=log_mel_features/linear_to_mel_weight_matrix/frame/zeros_like�
Blog_mel_features/linear_to_mel_weight_matrix/frame/ones_like/ShapeConst*
_output_shapes
:*
dtype0*
valueB:2D
Blog_mel_features/linear_to_mel_weight_matrix/frame/ones_like/Shape�
Blog_mel_features/linear_to_mel_weight_matrix/frame/ones_like/ConstConst*
_output_shapes
: *
dtype0*
value	B :2D
Blog_mel_features/linear_to_mel_weight_matrix/frame/ones_like/Const�
<log_mel_features/linear_to_mel_weight_matrix/frame/ones_likeFillKlog_mel_features/linear_to_mel_weight_matrix/frame/ones_like/Shape:output:0Klog_mel_features/linear_to_mel_weight_matrix/frame/ones_like/Const:output:0*
T0*
_output_shapes
:2>
<log_mel_features/linear_to_mel_weight_matrix/frame/ones_like�
?log_mel_features/linear_to_mel_weight_matrix/frame/StridedSliceStridedSliceFlog_mel_features/linear_to_mel_weight_matrix/linspace_1/Slice:output:0Flog_mel_features/linear_to_mel_weight_matrix/frame/zeros_like:output:0Blog_mel_features/linear_to_mel_weight_matrix/frame/concat:output:0Elog_mel_features/linear_to_mel_weight_matrix/frame/ones_like:output:0*
Index0*
T0*
_output_shapes
:B2A
?log_mel_features/linear_to_mel_weight_matrix/frame/StridedSlice�
:log_mel_features/linear_to_mel_weight_matrix/frame/ReshapeReshapeHlog_mel_features/linear_to_mel_weight_matrix/frame/StridedSlice:output:0Dlog_mel_features/linear_to_mel_weight_matrix/frame/concat_1:output:0*
T0*
_output_shapes

:B2<
:log_mel_features/linear_to_mel_weight_matrix/frame/Reshape�
>log_mel_features/linear_to_mel_weight_matrix/frame/range/startConst*
_output_shapes
: *
dtype0*
value	B : 2@
>log_mel_features/linear_to_mel_weight_matrix/frame/range/start�
>log_mel_features/linear_to_mel_weight_matrix/frame/range/deltaConst*
_output_shapes
: *
dtype0*
value	B :2@
>log_mel_features/linear_to_mel_weight_matrix/frame/range/delta�
8log_mel_features/linear_to_mel_weight_matrix/frame/rangeRangeGlog_mel_features/linear_to_mel_weight_matrix/frame/range/start:output:0>log_mel_features/linear_to_mel_weight_matrix/frame/Maximum:z:0Glog_mel_features/linear_to_mel_weight_matrix/frame/range/delta:output:0*
_output_shapes
:@2:
8log_mel_features/linear_to_mel_weight_matrix/frame/range�
6log_mel_features/linear_to_mel_weight_matrix/frame/mulMulAlog_mel_features/linear_to_mel_weight_matrix/frame/range:output:0Alog_mel_features/linear_to_mel_weight_matrix/frame/floordiv_2:z:0*
T0*
_output_shapes
:@28
6log_mel_features/linear_to_mel_weight_matrix/frame/mul�
Dlog_mel_features/linear_to_mel_weight_matrix/frame/Reshape_1/shape/1Const*
_output_shapes
: *
dtype0*
value	B :2F
Dlog_mel_features/linear_to_mel_weight_matrix/frame/Reshape_1/shape/1�
Blog_mel_features/linear_to_mel_weight_matrix/frame/Reshape_1/shapePack>log_mel_features/linear_to_mel_weight_matrix/frame/Maximum:z:0Mlog_mel_features/linear_to_mel_weight_matrix/frame/Reshape_1/shape/1:output:0*
N*
T0*
_output_shapes
:2D
Blog_mel_features/linear_to_mel_weight_matrix/frame/Reshape_1/shape�
<log_mel_features/linear_to_mel_weight_matrix/frame/Reshape_1Reshape:log_mel_features/linear_to_mel_weight_matrix/frame/mul:z:0Klog_mel_features/linear_to_mel_weight_matrix/frame/Reshape_1/shape:output:0*
T0*
_output_shapes

:@2>
<log_mel_features/linear_to_mel_weight_matrix/frame/Reshape_1�
@log_mel_features/linear_to_mel_weight_matrix/frame/range_1/startConst*
_output_shapes
: *
dtype0*
value	B : 2B
@log_mel_features/linear_to_mel_weight_matrix/frame/range_1/start�
@log_mel_features/linear_to_mel_weight_matrix/frame/range_1/deltaConst*
_output_shapes
: *
dtype0*
value	B :2B
@log_mel_features/linear_to_mel_weight_matrix/frame/range_1/delta�
:log_mel_features/linear_to_mel_weight_matrix/frame/range_1RangeIlog_mel_features/linear_to_mel_weight_matrix/frame/range_1/start:output:0Alog_mel_features/linear_to_mel_weight_matrix/frame/floordiv_1:z:0Ilog_mel_features/linear_to_mel_weight_matrix/frame/range_1/delta:output:0*
_output_shapes
:2<
:log_mel_features/linear_to_mel_weight_matrix/frame/range_1�
Dlog_mel_features/linear_to_mel_weight_matrix/frame/Reshape_2/shape/0Const*
_output_shapes
: *
dtype0*
value	B :2F
Dlog_mel_features/linear_to_mel_weight_matrix/frame/Reshape_2/shape/0�
Blog_mel_features/linear_to_mel_weight_matrix/frame/Reshape_2/shapePackMlog_mel_features/linear_to_mel_weight_matrix/frame/Reshape_2/shape/0:output:0Alog_mel_features/linear_to_mel_weight_matrix/frame/floordiv_1:z:0*
N*
T0*
_output_shapes
:2D
Blog_mel_features/linear_to_mel_weight_matrix/frame/Reshape_2/shape�
<log_mel_features/linear_to_mel_weight_matrix/frame/Reshape_2ReshapeClog_mel_features/linear_to_mel_weight_matrix/frame/range_1:output:0Klog_mel_features/linear_to_mel_weight_matrix/frame/Reshape_2/shape:output:0*
T0*
_output_shapes

:2>
<log_mel_features/linear_to_mel_weight_matrix/frame/Reshape_2�
8log_mel_features/linear_to_mel_weight_matrix/frame/add_1AddV2Elog_mel_features/linear_to_mel_weight_matrix/frame/Reshape_1:output:0Elog_mel_features/linear_to_mel_weight_matrix/frame/Reshape_2:output:0*
T0*
_output_shapes

:@2:
8log_mel_features/linear_to_mel_weight_matrix/frame/add_1�
@log_mel_features/linear_to_mel_weight_matrix/frame/GatherV2/axisConst*
_output_shapes
: *
dtype0*
value	B : 2B
@log_mel_features/linear_to_mel_weight_matrix/frame/GatherV2/axis�
;log_mel_features/linear_to_mel_weight_matrix/frame/GatherV2GatherV2Clog_mel_features/linear_to_mel_weight_matrix/frame/Reshape:output:0<log_mel_features/linear_to_mel_weight_matrix/frame/add_1:z:0Ilog_mel_features/linear_to_mel_weight_matrix/frame/GatherV2/axis:output:0*
Taxis0*
Tindices0*
Tparams0*"
_output_shapes
:@2=
;log_mel_features/linear_to_mel_weight_matrix/frame/GatherV2�
Dlog_mel_features/linear_to_mel_weight_matrix/frame/concat_2/values_0Const*
_output_shapes
: *
dtype0*
valueB 2F
Dlog_mel_features/linear_to_mel_weight_matrix/frame/concat_2/values_0�
Dlog_mel_features/linear_to_mel_weight_matrix/frame/concat_2/values_1Pack>log_mel_features/linear_to_mel_weight_matrix/frame/Maximum:z:0Hlog_mel_features/linear_to_mel_weight_matrix/frame/frame_length:output:0*
N*
T0*
_output_shapes
:2F
Dlog_mel_features/linear_to_mel_weight_matrix/frame/concat_2/values_1�
Dlog_mel_features/linear_to_mel_weight_matrix/frame/concat_2/values_2Const*
_output_shapes
: *
dtype0*
valueB 2F
Dlog_mel_features/linear_to_mel_weight_matrix/frame/concat_2/values_2�
@log_mel_features/linear_to_mel_weight_matrix/frame/concat_2/axisConst*
_output_shapes
: *
dtype0*
value	B : 2B
@log_mel_features/linear_to_mel_weight_matrix/frame/concat_2/axis�
;log_mel_features/linear_to_mel_weight_matrix/frame/concat_2ConcatV2Mlog_mel_features/linear_to_mel_weight_matrix/frame/concat_2/values_0:output:0Mlog_mel_features/linear_to_mel_weight_matrix/frame/concat_2/values_1:output:0Mlog_mel_features/linear_to_mel_weight_matrix/frame/concat_2/values_2:output:0Ilog_mel_features/linear_to_mel_weight_matrix/frame/concat_2/axis:output:0*
N*
T0*
_output_shapes
:2=
;log_mel_features/linear_to_mel_weight_matrix/frame/concat_2�
<log_mel_features/linear_to_mel_weight_matrix/frame/Reshape_3ReshapeDlog_mel_features/linear_to_mel_weight_matrix/frame/GatherV2:output:0Dlog_mel_features/linear_to_mel_weight_matrix/frame/concat_2:output:0*
T0*
_output_shapes

:@2>
<log_mel_features/linear_to_mel_weight_matrix/frame/Reshape_3�
4log_mel_features/linear_to_mel_weight_matrix/Const_1Const*
_output_shapes
: *
dtype0*
value	B :26
4log_mel_features/linear_to_mel_weight_matrix/Const_1�
<log_mel_features/linear_to_mel_weight_matrix/split/split_dimConst*
_output_shapes
: *
dtype0*
value	B :2>
<log_mel_features/linear_to_mel_weight_matrix/split/split_dim�
2log_mel_features/linear_to_mel_weight_matrix/splitSplitElog_mel_features/linear_to_mel_weight_matrix/split/split_dim:output:0Elog_mel_features/linear_to_mel_weight_matrix/frame/Reshape_3:output:0*
T0*2
_output_shapes 
:@:@:@*
	num_split24
2log_mel_features/linear_to_mel_weight_matrix/split�
:log_mel_features/linear_to_mel_weight_matrix/Reshape/shapeConst*
_output_shapes
:*
dtype0*
valueB"   @   2<
:log_mel_features/linear_to_mel_weight_matrix/Reshape/shape�
4log_mel_features/linear_to_mel_weight_matrix/ReshapeReshape;log_mel_features/linear_to_mel_weight_matrix/split:output:0Clog_mel_features/linear_to_mel_weight_matrix/Reshape/shape:output:0*
T0*
_output_shapes

:@26
4log_mel_features/linear_to_mel_weight_matrix/Reshape�
<log_mel_features/linear_to_mel_weight_matrix/Reshape_1/shapeConst*
_output_shapes
:*
dtype0*
valueB"   @   2>
<log_mel_features/linear_to_mel_weight_matrix/Reshape_1/shape�
6log_mel_features/linear_to_mel_weight_matrix/Reshape_1Reshape;log_mel_features/linear_to_mel_weight_matrix/split:output:1Elog_mel_features/linear_to_mel_weight_matrix/Reshape_1/shape:output:0*
T0*
_output_shapes

:@28
6log_mel_features/linear_to_mel_weight_matrix/Reshape_1�
<log_mel_features/linear_to_mel_weight_matrix/Reshape_2/shapeConst*
_output_shapes
:*
dtype0*
valueB"   @   2>
<log_mel_features/linear_to_mel_weight_matrix/Reshape_2/shape�
6log_mel_features/linear_to_mel_weight_matrix/Reshape_2Reshape;log_mel_features/linear_to_mel_weight_matrix/split:output:2Elog_mel_features/linear_to_mel_weight_matrix/Reshape_2/shape:output:0*
T0*
_output_shapes

:@28
6log_mel_features/linear_to_mel_weight_matrix/Reshape_2�
0log_mel_features/linear_to_mel_weight_matrix/subSub@log_mel_features/linear_to_mel_weight_matrix/ExpandDims:output:0=log_mel_features/linear_to_mel_weight_matrix/Reshape:output:0*
T0*
_output_shapes
:	�@22
0log_mel_features/linear_to_mel_weight_matrix/sub�
2log_mel_features/linear_to_mel_weight_matrix/sub_1Sub?log_mel_features/linear_to_mel_weight_matrix/Reshape_1:output:0=log_mel_features/linear_to_mel_weight_matrix/Reshape:output:0*
T0*
_output_shapes

:@24
2log_mel_features/linear_to_mel_weight_matrix/sub_1�
6log_mel_features/linear_to_mel_weight_matrix/truediv_1RealDiv4log_mel_features/linear_to_mel_weight_matrix/sub:z:06log_mel_features/linear_to_mel_weight_matrix/sub_1:z:0*
T0*
_output_shapes
:	�@28
6log_mel_features/linear_to_mel_weight_matrix/truediv_1�
2log_mel_features/linear_to_mel_weight_matrix/sub_2Sub?log_mel_features/linear_to_mel_weight_matrix/Reshape_2:output:0@log_mel_features/linear_to_mel_weight_matrix/ExpandDims:output:0*
T0*
_output_shapes
:	�@24
2log_mel_features/linear_to_mel_weight_matrix/sub_2�
2log_mel_features/linear_to_mel_weight_matrix/sub_3Sub?log_mel_features/linear_to_mel_weight_matrix/Reshape_2:output:0?log_mel_features/linear_to_mel_weight_matrix/Reshape_1:output:0*
T0*
_output_shapes

:@24
2log_mel_features/linear_to_mel_weight_matrix/sub_3�
6log_mel_features/linear_to_mel_weight_matrix/truediv_2RealDiv6log_mel_features/linear_to_mel_weight_matrix/sub_2:z:06log_mel_features/linear_to_mel_weight_matrix/sub_3:z:0*
T0*
_output_shapes
:	�@28
6log_mel_features/linear_to_mel_weight_matrix/truediv_2�
4log_mel_features/linear_to_mel_weight_matrix/MinimumMinimum:log_mel_features/linear_to_mel_weight_matrix/truediv_1:z:0:log_mel_features/linear_to_mel_weight_matrix/truediv_2:z:0*
T0*
_output_shapes
:	�@26
4log_mel_features/linear_to_mel_weight_matrix/Minimum�
4log_mel_features/linear_to_mel_weight_matrix/MaximumMaximum;log_mel_features/linear_to_mel_weight_matrix/Const:output:08log_mel_features/linear_to_mel_weight_matrix/Minimum:z:0*
T0*
_output_shapes
:	�@26
4log_mel_features/linear_to_mel_weight_matrix/Maximum�
5log_mel_features/linear_to_mel_weight_matrix/paddingsConst*
_output_shapes

:*
dtype0*)
value B"               27
5log_mel_features/linear_to_mel_weight_matrix/paddings�
,log_mel_features/linear_to_mel_weight_matrixPad8log_mel_features/linear_to_mel_weight_matrix/Maximum:z:0>log_mel_features/linear_to_mel_weight_matrix/paddings:output:0*
T0*
_output_shapes
:	�@2.
,log_mel_features/linear_to_mel_weight_matrix�
log_mel_features/MatMulMatMullog_mel_features/Abs:y:05log_mel_features/linear_to_mel_weight_matrix:output:0*
T0*'
_output_shapes
:���������@2
log_mel_features/MatMulu
log_mel_features/add/yConst*
_output_shapes
: *
dtype0*
valueB
 *
�#<2
log_mel_features/add/y�
log_mel_features/addAddV2!log_mel_features/MatMul:product:0log_mel_features/add/y:output:0*
T0*'
_output_shapes
:���������@2
log_mel_features/add
log_mel_features/LogLoglog_mel_features/add:z:0*
T0*'
_output_shapes
:���������@2
log_mel_features/Log�
#log_mel_features/frame/frame_lengthConst*
_output_shapes
: *
dtype0*
value	B :`2%
#log_mel_features/frame/frame_length�
!log_mel_features/frame/frame_stepConst*
_output_shapes
: *
dtype0*
value	B :`2#
!log_mel_features/frame/frame_step|
log_mel_features/frame/axisConst*
_output_shapes
: *
dtype0*
value	B : 2
log_mel_features/frame/axis�
log_mel_features/frame/ShapeShapelog_mel_features/Log:y:0*
T0*
_output_shapes
:2
log_mel_features/frame/Shape:��|
log_mel_features/frame/RankConst*
_output_shapes
: *
dtype0*
value	B :2
log_mel_features/frame/Rank�
"log_mel_features/frame/range/startConst*
_output_shapes
: *
dtype0*
value	B : 2$
"log_mel_features/frame/range/start�
"log_mel_features/frame/range/deltaConst*
_output_shapes
: *
dtype0*
value	B :2$
"log_mel_features/frame/range/delta�
log_mel_features/frame/rangeRange+log_mel_features/frame/range/start:output:0$log_mel_features/frame/Rank:output:0+log_mel_features/frame/range/delta:output:0*
_output_shapes
:2
log_mel_features/frame/range�
*log_mel_features/frame/strided_slice/stackConst*
_output_shapes
:*
dtype0*
valueB: 2,
*log_mel_features/frame/strided_slice/stack�
,log_mel_features/frame/strided_slice/stack_1Const*
_output_shapes
:*
dtype0*
valueB:2.
,log_mel_features/frame/strided_slice/stack_1�
,log_mel_features/frame/strided_slice/stack_2Const*
_output_shapes
:*
dtype0*
valueB:2.
,log_mel_features/frame/strided_slice/stack_2�
$log_mel_features/frame/strided_sliceStridedSlice%log_mel_features/frame/range:output:03log_mel_features/frame/strided_slice/stack:output:05log_mel_features/frame/strided_slice/stack_1:output:05log_mel_features/frame/strided_slice/stack_2:output:0*
Index0*
T0*
_output_shapes
: *
shrink_axis_mask2&
$log_mel_features/frame/strided_slice~
log_mel_features/frame/sub/yConst*
_output_shapes
: *
dtype0*
value	B :2
log_mel_features/frame/sub/y�
log_mel_features/frame/subSub$log_mel_features/frame/Rank:output:0%log_mel_features/frame/sub/y:output:0*
T0*
_output_shapes
: 2
log_mel_features/frame/sub�
log_mel_features/frame/sub_1Sublog_mel_features/frame/sub:z:0-log_mel_features/frame/strided_slice:output:0*
T0*
_output_shapes
: 2
log_mel_features/frame/sub_1�
log_mel_features/frame/packed/1Const*
_output_shapes
: *
dtype0*
value	B :2!
log_mel_features/frame/packed/1�
log_mel_features/frame/packedPack-log_mel_features/frame/strided_slice:output:0(log_mel_features/frame/packed/1:output:0 log_mel_features/frame/sub_1:z:0*
N*
T0*
_output_shapes
:2
log_mel_features/frame/packed�
&log_mel_features/frame/split/split_dimConst*
_output_shapes
: *
dtype0*
value	B : 2(
&log_mel_features/frame/split/split_dim�
log_mel_features/frame/splitSplitV%log_mel_features/frame/Shape:output:0&log_mel_features/frame/packed:output:0/log_mel_features/frame/split/split_dim:output:0*

Tlen0*
T0*$
_output_shapes
: ::*
	num_split2
log_mel_features/frame/split�
$log_mel_features/frame/Reshape/shapeConst*
_output_shapes
: *
dtype0*
valueB 2&
$log_mel_features/frame/Reshape/shape�
log_mel_features/frame/ReshapeReshape%log_mel_features/frame/split:output:1-log_mel_features/frame/Reshape/shape:output:0*
T0*
_output_shapes
: 2 
log_mel_features/frame/Reshape|
log_mel_features/frame/SizeConst*
_output_shapes
: *
dtype0*
value	B : 2
log_mel_features/frame/Size�
log_mel_features/frame/Size_1Const*
_output_shapes
: *
dtype0*
value	B :2
log_mel_features/frame/Size_1�
log_mel_features/frame/sub_2Sub'log_mel_features/frame/Reshape:output:0,log_mel_features/frame/frame_length:output:0*
T0*
_output_shapes
: 2
log_mel_features/frame/sub_2�
log_mel_features/frame/floordivFloorDiv log_mel_features/frame/sub_2:z:0*log_mel_features/frame/frame_step:output:0*
T0*
_output_shapes
: 2!
log_mel_features/frame/floordiv~
log_mel_features/frame/add/xConst*
_output_shapes
: *
dtype0*
value	B :2
log_mel_features/frame/add/x�
log_mel_features/frame/addAddV2%log_mel_features/frame/add/x:output:0#log_mel_features/frame/floordiv:z:0*
T0*
_output_shapes
: 2
log_mel_features/frame/add�
 log_mel_features/frame/Maximum/xConst*
_output_shapes
: *
dtype0*
value	B : 2"
 log_mel_features/frame/Maximum/x�
log_mel_features/frame/MaximumMaximum)log_mel_features/frame/Maximum/x:output:0log_mel_features/frame/add:z:0*
T0*
_output_shapes
: 2 
log_mel_features/frame/Maximum�
 log_mel_features/frame/gcd/ConstConst*
_output_shapes
: *
dtype0*
value	B :`2"
 log_mel_features/frame/gcd/Const�
#log_mel_features/frame/floordiv_1/yConst*
_output_shapes
: *
dtype0*
value	B :`2%
#log_mel_features/frame/floordiv_1/y�
!log_mel_features/frame/floordiv_1FloorDiv,log_mel_features/frame/frame_length:output:0,log_mel_features/frame/floordiv_1/y:output:0*
T0*
_output_shapes
: 2#
!log_mel_features/frame/floordiv_1�
#log_mel_features/frame/floordiv_2/yConst*
_output_shapes
: *
dtype0*
value	B :`2%
#log_mel_features/frame/floordiv_2/y�
!log_mel_features/frame/floordiv_2FloorDiv*log_mel_features/frame/frame_step:output:0,log_mel_features/frame/floordiv_2/y:output:0*
T0*
_output_shapes
: 2#
!log_mel_features/frame/floordiv_2�
#log_mel_features/frame/floordiv_3/yConst*
_output_shapes
: *
dtype0*
value	B :`2%
#log_mel_features/frame/floordiv_3/y�
!log_mel_features/frame/floordiv_3FloorDiv'log_mel_features/frame/Reshape:output:0,log_mel_features/frame/floordiv_3/y:output:0*
T0*
_output_shapes
: 2#
!log_mel_features/frame/floordiv_3~
log_mel_features/frame/mul/yConst*
_output_shapes
: *
dtype0*
value	B :`2
log_mel_features/frame/mul/y�
log_mel_features/frame/mulMul%log_mel_features/frame/floordiv_3:z:0%log_mel_features/frame/mul/y:output:0*
T0*
_output_shapes
: 2
log_mel_features/frame/mul�
&log_mel_features/frame/concat/values_1Packlog_mel_features/frame/mul:z:0*
N*
T0*
_output_shapes
:2(
&log_mel_features/frame/concat/values_1�
"log_mel_features/frame/concat/axisConst*
_output_shapes
: *
dtype0*
value	B : 2$
"log_mel_features/frame/concat/axis�
log_mel_features/frame/concatConcatV2%log_mel_features/frame/split:output:0/log_mel_features/frame/concat/values_1:output:0%log_mel_features/frame/split:output:2+log_mel_features/frame/concat/axis:output:0*
N*
T0*
_output_shapes
:2
log_mel_features/frame/concat�
*log_mel_features/frame/concat_1/values_1/1Const*
_output_shapes
: *
dtype0*
value	B :`2,
*log_mel_features/frame/concat_1/values_1/1�
(log_mel_features/frame/concat_1/values_1Pack%log_mel_features/frame/floordiv_3:z:03log_mel_features/frame/concat_1/values_1/1:output:0*
N*
T0*
_output_shapes
:2*
(log_mel_features/frame/concat_1/values_1�
$log_mel_features/frame/concat_1/axisConst*
_output_shapes
: *
dtype0*
value	B : 2&
$log_mel_features/frame/concat_1/axis�
log_mel_features/frame/concat_1ConcatV2%log_mel_features/frame/split:output:01log_mel_features/frame/concat_1/values_1:output:0%log_mel_features/frame/split:output:2-log_mel_features/frame/concat_1/axis:output:0*
N*
T0*
_output_shapes
:2!
log_mel_features/frame/concat_1�
!log_mel_features/frame/zeros_likeConst*
_output_shapes
:*
dtype0*
valueB: 2#
!log_mel_features/frame/zeros_like�
&log_mel_features/frame/ones_like/ShapeConst*
_output_shapes
:*
dtype0*
valueB:2(
&log_mel_features/frame/ones_like/Shape�
&log_mel_features/frame/ones_like/ConstConst*
_output_shapes
: *
dtype0*
value	B :2(
&log_mel_features/frame/ones_like/Const�
 log_mel_features/frame/ones_likeFill/log_mel_features/frame/ones_like/Shape:output:0/log_mel_features/frame/ones_like/Const:output:0*
T0*
_output_shapes
:2"
 log_mel_features/frame/ones_like�
#log_mel_features/frame/StridedSliceStridedSlicelog_mel_features/Log:y:0*log_mel_features/frame/zeros_like:output:0&log_mel_features/frame/concat:output:0)log_mel_features/frame/ones_like:output:0*
Index0*
T0*0
_output_shapes
:������������������2%
#log_mel_features/frame/StridedSlice�
 log_mel_features/frame/Reshape_1Reshape,log_mel_features/frame/StridedSlice:output:0(log_mel_features/frame/concat_1:output:0*
T0*4
_output_shapes"
 :���������`���������2"
 log_mel_features/frame/Reshape_1�
$log_mel_features/frame/range_1/startConst*
_output_shapes
: *
dtype0*
value	B : 2&
$log_mel_features/frame/range_1/start�
$log_mel_features/frame/range_1/deltaConst*
_output_shapes
: *
dtype0*
value	B :2&
$log_mel_features/frame/range_1/delta�
log_mel_features/frame/range_1Range-log_mel_features/frame/range_1/start:output:0"log_mel_features/frame/Maximum:z:0-log_mel_features/frame/range_1/delta:output:0*#
_output_shapes
:���������2 
log_mel_features/frame/range_1�
log_mel_features/frame/mul_1Mul'log_mel_features/frame/range_1:output:0%log_mel_features/frame/floordiv_2:z:0*
T0*#
_output_shapes
:���������2
log_mel_features/frame/mul_1�
(log_mel_features/frame/Reshape_2/shape/1Const*
_output_shapes
: *
dtype0*
value	B :2*
(log_mel_features/frame/Reshape_2/shape/1�
&log_mel_features/frame/Reshape_2/shapePack"log_mel_features/frame/Maximum:z:01log_mel_features/frame/Reshape_2/shape/1:output:0*
N*
T0*
_output_shapes
:2(
&log_mel_features/frame/Reshape_2/shape�
 log_mel_features/frame/Reshape_2Reshape log_mel_features/frame/mul_1:z:0/log_mel_features/frame/Reshape_2/shape:output:0*
T0*'
_output_shapes
:���������2"
 log_mel_features/frame/Reshape_2�
$log_mel_features/frame/range_2/startConst*
_output_shapes
: *
dtype0*
value	B : 2&
$log_mel_features/frame/range_2/start�
$log_mel_features/frame/range_2/deltaConst*
_output_shapes
: *
dtype0*
value	B :2&
$log_mel_features/frame/range_2/delta�
log_mel_features/frame/range_2Range-log_mel_features/frame/range_2/start:output:0%log_mel_features/frame/floordiv_1:z:0-log_mel_features/frame/range_2/delta:output:0*
_output_shapes
:2 
log_mel_features/frame/range_2�
(log_mel_features/frame/Reshape_3/shape/0Const*
_output_shapes
: *
dtype0*
value	B :2*
(log_mel_features/frame/Reshape_3/shape/0�
&log_mel_features/frame/Reshape_3/shapePack1log_mel_features/frame/Reshape_3/shape/0:output:0%log_mel_features/frame/floordiv_1:z:0*
N*
T0*
_output_shapes
:2(
&log_mel_features/frame/Reshape_3/shape�
 log_mel_features/frame/Reshape_3Reshape'log_mel_features/frame/range_2:output:0/log_mel_features/frame/Reshape_3/shape:output:0*
T0*
_output_shapes

:2"
 log_mel_features/frame/Reshape_3�
log_mel_features/frame/add_1AddV2)log_mel_features/frame/Reshape_2:output:0)log_mel_features/frame/Reshape_3:output:0*
T0*'
_output_shapes
:���������2
log_mel_features/frame/add_1�
log_mel_features/frame/GatherV2GatherV2)log_mel_features/frame/Reshape_1:output:0 log_mel_features/frame/add_1:z:0-log_mel_features/frame/strided_slice:output:0*
Taxis0*
Tindices0*
Tparams0*8
_output_shapes&
$:"���������`���������2!
log_mel_features/frame/GatherV2�
(log_mel_features/frame/concat_2/values_1Pack"log_mel_features/frame/Maximum:z:0,log_mel_features/frame/frame_length:output:0*
N*
T0*
_output_shapes
:2*
(log_mel_features/frame/concat_2/values_1�
$log_mel_features/frame/concat_2/axisConst*
_output_shapes
: *
dtype0*
value	B : 2&
$log_mel_features/frame/concat_2/axis�
log_mel_features/frame/concat_2ConcatV2%log_mel_features/frame/split:output:01log_mel_features/frame/concat_2/values_1:output:0%log_mel_features/frame/split:output:2-log_mel_features/frame/concat_2/axis:output:0*
N*
T0*
_output_shapes
:2!
log_mel_features/frame/concat_2�
 log_mel_features/frame/Reshape_4Reshape(log_mel_features/frame/GatherV2:output:0(log_mel_features/frame/concat_2:output:0*
T0*+
_output_shapes
:���������`@2"
 log_mel_features/frame/Reshape_4�
vggish/Reshape/shapeConst*
_output_shapes
:*
dtype0*%
valueB"����`   @      2
vggish/Reshape/shape�
vggish/ReshapeReshape)log_mel_features/frame/Reshape_4:output:0vggish/Reshape/shape:output:0*
T0*/
_output_shapes
:���������`@2
vggish/Reshape�
"vggish/conv1/Conv2D/ReadVariableOpReadVariableOp+vggish_conv1_conv2d_readvariableop_resource*&
_output_shapes
:@*
dtype02$
"vggish/conv1/Conv2D/ReadVariableOp�
vggish/conv1/Conv2DConv2Dvggish/Reshape:output:0*vggish/conv1/Conv2D/ReadVariableOp:value:0*
T0*/
_output_shapes
:���������`@@*
paddingSAME*
strides
2
vggish/conv1/Conv2D�
#vggish/conv1/BiasAdd/ReadVariableOpReadVariableOp,vggish_conv1_biasadd_readvariableop_resource*
_output_shapes
:@*
dtype02%
#vggish/conv1/BiasAdd/ReadVariableOp�
vggish/conv1/BiasAddBiasAddvggish/conv1/Conv2D:output:0+vggish/conv1/BiasAdd/ReadVariableOp:value:0*
T0*/
_output_shapes
:���������`@@2
vggish/conv1/BiasAdd�
vggish/conv1/ReluReluvggish/conv1/BiasAdd:output:0*
T0*/
_output_shapes
:���������`@@2
vggish/conv1/Relu�
vggish/pool1/MaxPoolMaxPoolvggish/conv1/Relu:activations:0*/
_output_shapes
:���������0 @*
ksize
*
paddingSAME*
strides
2
vggish/pool1/MaxPool�
"vggish/conv2/Conv2D/ReadVariableOpReadVariableOp+vggish_conv2_conv2d_readvariableop_resource*'
_output_shapes
:@�*
dtype02$
"vggish/conv2/Conv2D/ReadVariableOp�
vggish/conv2/Conv2DConv2Dvggish/pool1/MaxPool:output:0*vggish/conv2/Conv2D/ReadVariableOp:value:0*
T0*0
_output_shapes
:���������0 �*
paddingSAME*
strides
2
vggish/conv2/Conv2D�
#vggish/conv2/BiasAdd/ReadVariableOpReadVariableOp,vggish_conv2_biasadd_readvariableop_resource*
_output_shapes	
:�*
dtype02%
#vggish/conv2/BiasAdd/ReadVariableOp�
vggish/conv2/BiasAddBiasAddvggish/conv2/Conv2D:output:0+vggish/conv2/BiasAdd/ReadVariableOp:value:0*
T0*0
_output_shapes
:���������0 �2
vggish/conv2/BiasAdd�
vggish/conv2/ReluReluvggish/conv2/BiasAdd:output:0*
T0*0
_output_shapes
:���������0 �2
vggish/conv2/Relu�
vggish/pool2/MaxPoolMaxPoolvggish/conv2/Relu:activations:0*0
_output_shapes
:����������*
ksize
*
paddingSAME*
strides
2
vggish/pool2/MaxPool�
*vggish/conv3/conv3_1/Conv2D/ReadVariableOpReadVariableOp3vggish_conv3_conv3_1_conv2d_readvariableop_resource*(
_output_shapes
:��*
dtype02,
*vggish/conv3/conv3_1/Conv2D/ReadVariableOp�
vggish/conv3/conv3_1/Conv2DConv2Dvggish/pool2/MaxPool:output:02vggish/conv3/conv3_1/Conv2D/ReadVariableOp:value:0*
T0*0
_output_shapes
:����������*
paddingSAME*
strides
2
vggish/conv3/conv3_1/Conv2D�
+vggish/conv3/conv3_1/BiasAdd/ReadVariableOpReadVariableOp4vggish_conv3_conv3_1_biasadd_readvariableop_resource*
_output_shapes	
:�*
dtype02-
+vggish/conv3/conv3_1/BiasAdd/ReadVariableOp�
vggish/conv3/conv3_1/BiasAddBiasAdd$vggish/conv3/conv3_1/Conv2D:output:03vggish/conv3/conv3_1/BiasAdd/ReadVariableOp:value:0*
T0*0
_output_shapes
:����������2
vggish/conv3/conv3_1/BiasAdd�
vggish/conv3/conv3_1/ReluRelu%vggish/conv3/conv3_1/BiasAdd:output:0*
T0*0
_output_shapes
:����������2
vggish/conv3/conv3_1/Relu�
*vggish/conv3/conv3_2/Conv2D/ReadVariableOpReadVariableOp3vggish_conv3_conv3_2_conv2d_readvariableop_resource*(
_output_shapes
:��*
dtype02,
*vggish/conv3/conv3_2/Conv2D/ReadVariableOp�
vggish/conv3/conv3_2/Conv2DConv2D'vggish/conv3/conv3_1/Relu:activations:02vggish/conv3/conv3_2/Conv2D/ReadVariableOp:value:0*
T0*0
_output_shapes
:����������*
paddingSAME*
strides
2
vggish/conv3/conv3_2/Conv2D�
+vggish/conv3/conv3_2/BiasAdd/ReadVariableOpReadVariableOp4vggish_conv3_conv3_2_biasadd_readvariableop_resource*
_output_shapes	
:�*
dtype02-
+vggish/conv3/conv3_2/BiasAdd/ReadVariableOp�
vggish/conv3/conv3_2/BiasAddBiasAdd$vggish/conv3/conv3_2/Conv2D:output:03vggish/conv3/conv3_2/BiasAdd/ReadVariableOp:value:0*
T0*0
_output_shapes
:����������2
vggish/conv3/conv3_2/BiasAdd�
vggish/conv3/conv3_2/ReluRelu%vggish/conv3/conv3_2/BiasAdd:output:0*
T0*0
_output_shapes
:����������2
vggish/conv3/conv3_2/Relu�
vggish/pool3/MaxPoolMaxPool'vggish/conv3/conv3_2/Relu:activations:0*0
_output_shapes
:����������*
ksize
*
paddingSAME*
strides
2
vggish/pool3/MaxPool�
*vggish/conv4/conv4_1/Conv2D/ReadVariableOpReadVariableOp3vggish_conv4_conv4_1_conv2d_readvariableop_resource*(
_output_shapes
:��*
dtype02,
*vggish/conv4/conv4_1/Conv2D/ReadVariableOp�
vggish/conv4/conv4_1/Conv2DConv2Dvggish/pool3/MaxPool:output:02vggish/conv4/conv4_1/Conv2D/ReadVariableOp:value:0*
T0*0
_output_shapes
:����������*
paddingSAME*
strides
2
vggish/conv4/conv4_1/Conv2D�
+vggish/conv4/conv4_1/BiasAdd/ReadVariableOpReadVariableOp4vggish_conv4_conv4_1_biasadd_readvariableop_resource*
_output_shapes	
:�*
dtype02-
+vggish/conv4/conv4_1/BiasAdd/ReadVariableOp�
vggish/conv4/conv4_1/BiasAddBiasAdd$vggish/conv4/conv4_1/Conv2D:output:03vggish/conv4/conv4_1/BiasAdd/ReadVariableOp:value:0*
T0*0
_output_shapes
:����������2
vggish/conv4/conv4_1/BiasAdd�
vggish/conv4/conv4_1/ReluRelu%vggish/conv4/conv4_1/BiasAdd:output:0*
T0*0
_output_shapes
:����������2
vggish/conv4/conv4_1/Relu�
*vggish/conv4/conv4_2/Conv2D/ReadVariableOpReadVariableOp3vggish_conv4_conv4_2_conv2d_readvariableop_resource*(
_output_shapes
:��*
dtype02,
*vggish/conv4/conv4_2/Conv2D/ReadVariableOp�
vggish/conv4/conv4_2/Conv2DConv2D'vggish/conv4/conv4_1/Relu:activations:02vggish/conv4/conv4_2/Conv2D/ReadVariableOp:value:0*
T0*0
_output_shapes
:����������*
paddingSAME*
strides
2
vggish/conv4/conv4_2/Conv2D�
+vggish/conv4/conv4_2/BiasAdd/ReadVariableOpReadVariableOp4vggish_conv4_conv4_2_biasadd_readvariableop_resource*
_output_shapes	
:�*
dtype02-
+vggish/conv4/conv4_2/BiasAdd/ReadVariableOp�
vggish/conv4/conv4_2/BiasAddBiasAdd$vggish/conv4/conv4_2/Conv2D:output:03vggish/conv4/conv4_2/BiasAdd/ReadVariableOp:value:0*
T0*0
_output_shapes
:����������2
vggish/conv4/conv4_2/BiasAdd�
vggish/conv4/conv4_2/ReluRelu%vggish/conv4/conv4_2/BiasAdd:output:0*
T0*0
_output_shapes
:����������2
vggish/conv4/conv4_2/Relu�
vggish/pool4/MaxPoolMaxPool'vggish/conv4/conv4_2/Relu:activations:0*0
_output_shapes
:����������*
ksize
*
paddingSAME*
strides
2
vggish/pool4/MaxPool�
vggish/Flatten/flatten/ConstConst*
_output_shapes
:*
dtype0*
valueB"���� 0  2
vggish/Flatten/flatten/Const�
vggish/Flatten/flatten/ReshapeReshapevggish/pool4/MaxPool:output:0%vggish/Flatten/flatten/Const:output:0*
T0*(
_output_shapes
:����������`2 
vggish/Flatten/flatten/Reshape�
&vggish/fc1/fc1_1/MatMul/ReadVariableOpReadVariableOp/vggish_fc1_fc1_1_matmul_readvariableop_resource* 
_output_shapes
:
�`� *
dtype02(
&vggish/fc1/fc1_1/MatMul/ReadVariableOp�
vggish/fc1/fc1_1/MatMulMatMul'vggish/Flatten/flatten/Reshape:output:0.vggish/fc1/fc1_1/MatMul/ReadVariableOp:value:0*
T0*(
_output_shapes
:���������� 2
vggish/fc1/fc1_1/MatMul�
'vggish/fc1/fc1_1/BiasAdd/ReadVariableOpReadVariableOp0vggish_fc1_fc1_1_biasadd_readvariableop_resource*
_output_shapes	
:� *
dtype02)
'vggish/fc1/fc1_1/BiasAdd/ReadVariableOp�
vggish/fc1/fc1_1/BiasAddBiasAdd!vggish/fc1/fc1_1/MatMul:product:0/vggish/fc1/fc1_1/BiasAdd/ReadVariableOp:value:0*
T0*(
_output_shapes
:���������� 2
vggish/fc1/fc1_1/BiasAdd�
vggish/fc1/fc1_1/ReluRelu!vggish/fc1/fc1_1/BiasAdd:output:0*
T0*(
_output_shapes
:���������� 2
vggish/fc1/fc1_1/Relu�
&vggish/fc1/fc1_2/MatMul/ReadVariableOpReadVariableOp/vggish_fc1_fc1_2_matmul_readvariableop_resource* 
_output_shapes
:
� � *
dtype02(
&vggish/fc1/fc1_2/MatMul/ReadVariableOp�
vggish/fc1/fc1_2/MatMulMatMul#vggish/fc1/fc1_1/Relu:activations:0.vggish/fc1/fc1_2/MatMul/ReadVariableOp:value:0*
T0*(
_output_shapes
:���������� 2
vggish/fc1/fc1_2/MatMul�
'vggish/fc1/fc1_2/BiasAdd/ReadVariableOpReadVariableOp0vggish_fc1_fc1_2_biasadd_readvariableop_resource*
_output_shapes	
:� *
dtype02)
'vggish/fc1/fc1_2/BiasAdd/ReadVariableOp�
vggish/fc1/fc1_2/BiasAddBiasAdd!vggish/fc1/fc1_2/MatMul:product:0/vggish/fc1/fc1_2/BiasAdd/ReadVariableOp:value:0*
T0*(
_output_shapes
:���������� 2
vggish/fc1/fc1_2/BiasAdd�
vggish/fc1/fc1_2/ReluRelu!vggish/fc1/fc1_2/BiasAdd:output:0*
T0*(
_output_shapes
:���������� 2
vggish/fc1/fc1_2/Relu�
 vggish/fc2/MatMul/ReadVariableOpReadVariableOp)vggish_fc2_matmul_readvariableop_resource* 
_output_shapes
:
� �*
dtype02"
 vggish/fc2/MatMul/ReadVariableOp�
vggish/fc2/MatMulMatMul#vggish/fc1/fc1_2/Relu:activations:0(vggish/fc2/MatMul/ReadVariableOp:value:0*
T0*(
_output_shapes
:����������2
vggish/fc2/MatMul�
!vggish/fc2/BiasAdd/ReadVariableOpReadVariableOp*vggish_fc2_biasadd_readvariableop_resource*
_output_shapes	
:�*
dtype02#
!vggish/fc2/BiasAdd/ReadVariableOp�
vggish/fc2/BiasAddBiasAddvggish/fc2/MatMul:product:0)vggish/fc2/BiasAdd/ReadVariableOp:value:0*
T0*(
_output_shapes
:����������2
vggish/fc2/BiasAdd�
vggish/embeddingIdentityvggish/fc2/BiasAdd:output:0*
T0*(
_output_shapes
:����������2
vggish/embedding"-
vggish_embeddingvggish/embedding:output:0*(
_construction_contextkEagerRuntime*j
_input_shapesY
W:���������:::::::::::::::::::) %
#
_output_shapes
:���������
�
�
__inference___call___503
waveform!
unknown:@
	unknown_0:@$
	unknown_1:@�
	unknown_2:	�%
	unknown_3:��
	unknown_4:	�%
	unknown_5:��
	unknown_6:	�%
	unknown_7:��
	unknown_8:	�%
	unknown_9:��

unknown_10:	�

unknown_11:
�`� 

unknown_12:	� 

unknown_13:
� � 

unknown_14:	� 

unknown_15:
� �

unknown_16:	�
identity��StatefulPartitionedCall�
StatefulPartitionedCallStatefulPartitionedCallwaveformunknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4	unknown_5	unknown_6	unknown_7	unknown_8	unknown_9
unknown_10
unknown_11
unknown_12
unknown_13
unknown_14
unknown_15
unknown_16*
Tin
2*
Tout
2*(
_output_shapes
:����������*4
_read_only_resource_inputs
	
*-
config_proto

CPU

GPU 2J 8� *)
f$R"
 __inference_wrapped_function_4802
StatefulPartitionedCall�
IdentityIdentity StatefulPartitionedCall:output:0^StatefulPartitionedCall*
T0*(
_output_shapes
:����������2

Identity"
identityIdentity:output:0*(
_construction_contextkEagerRuntime*j
_input_shapesY
W:���������::::::::::::::::::22
StatefulPartitionedCallStatefulPartitionedCall:M I
#
_output_shapes
:���������
"
_user_specified_name
waveform
�
�
&__inference_restored_function_body_755
waveform!
unknown:@
	unknown_0:@$
	unknown_1:@�
	unknown_2:	�%
	unknown_3:��
	unknown_4:	�%
	unknown_5:��
	unknown_6:	�%
	unknown_7:��
	unknown_8:	�%
	unknown_9:��

unknown_10:	�

unknown_11:
�`� 

unknown_12:	� 

unknown_13:
� � 

unknown_14:	� 

unknown_15:
� �

unknown_16:	�
identity��StatefulPartitionedCall�
StatefulPartitionedCallStatefulPartitionedCallwaveformunknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4	unknown_5	unknown_6	unknown_7	unknown_8	unknown_9
unknown_10
unknown_11
unknown_12
unknown_13
unknown_14
unknown_15
unknown_16*
Tin
2*
Tout
2*
_collective_manager_ids
 *(
_output_shapes
:����������*4
_read_only_resource_inputs
	
*2
config_proto" 

CPU

GPU 2J 8� �J *!
fR
__inference___call___503p
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*(
_output_shapes
:����������<
NoOpNoOp^StatefulPartitionedCall*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*F
_input_shapes5
3:���������: : : : : : : : : : : : : : : : : : 22
StatefulPartitionedCallStatefulPartitionedCall:#

_user_specified_name751:#

_user_specified_name749:#

_user_specified_name747:#

_user_specified_name745:#

_user_specified_name743:#

_user_specified_name741:#

_user_specified_name739:#

_user_specified_name737:#


_user_specified_name735:#	

_user_specified_name733:#

_user_specified_name731:#

_user_specified_name729:#

_user_specified_name727:#

_user_specified_name725:#

_user_specified_name723:#

_user_specified_name721:#

_user_specified_name719:#

_user_specified_name717:M I
#
_output_shapes
:���������
"
_user_specified_name
waveform
��
�
__inference__traced_save_927
file_prefixE
+read_disablecopyonread_vggish_conv1_weights:@:
,read_1_disablecopyonread_vggish_conv1_biases:@H
-read_2_disablecopyonread_vggish_conv2_weights:@�;
,read_3_disablecopyonread_vggish_conv2_biases:	�Q
5read_4_disablecopyonread_vggish_conv3_conv3_1_weights:��C
4read_5_disablecopyonread_vggish_conv3_conv3_1_biases:	�Q
5read_6_disablecopyonread_vggish_conv3_conv3_2_weights:��C
4read_7_disablecopyonread_vggish_conv3_conv3_2_biases:	�Q
5read_8_disablecopyonread_vggish_conv4_conv4_1_weights:��C
4read_9_disablecopyonread_vggish_conv4_conv4_1_biases:	�R
6read_10_disablecopyonread_vggish_conv4_conv4_2_weights:��D
5read_11_disablecopyonread_vggish_conv4_conv4_2_biases:	�F
2read_12_disablecopyonread_vggish_fc1_fc1_1_weights:
�`� @
1read_13_disablecopyonread_vggish_fc1_fc1_1_biases:	� F
2read_14_disablecopyonread_vggish_fc1_fc1_2_weights:
� � @
1read_15_disablecopyonread_vggish_fc1_fc1_2_biases:	� @
,read_16_disablecopyonread_vggish_fc2_weights:
� �:
+read_17_disablecopyonread_vggish_fc2_biases:	�
savev2_const
identity_37��MergeV2Checkpoints�Read/DisableCopyOnRead�Read/ReadVariableOp�Read_1/DisableCopyOnRead�Read_1/ReadVariableOp�Read_10/DisableCopyOnRead�Read_10/ReadVariableOp�Read_11/DisableCopyOnRead�Read_11/ReadVariableOp�Read_12/DisableCopyOnRead�Read_12/ReadVariableOp�Read_13/DisableCopyOnRead�Read_13/ReadVariableOp�Read_14/DisableCopyOnRead�Read_14/ReadVariableOp�Read_15/DisableCopyOnRead�Read_15/ReadVariableOp�Read_16/DisableCopyOnRead�Read_16/ReadVariableOp�Read_17/DisableCopyOnRead�Read_17/ReadVariableOp�Read_2/DisableCopyOnRead�Read_2/ReadVariableOp�Read_3/DisableCopyOnRead�Read_3/ReadVariableOp�Read_4/DisableCopyOnRead�Read_4/ReadVariableOp�Read_5/DisableCopyOnRead�Read_5/ReadVariableOp�Read_6/DisableCopyOnRead�Read_6/ReadVariableOp�Read_7/DisableCopyOnRead�Read_7/ReadVariableOp�Read_8/DisableCopyOnRead�Read_8/ReadVariableOp�Read_9/DisableCopyOnRead�Read_9/ReadVariableOpw
StaticRegexFullMatchStaticRegexFullMatchfile_prefix"/device:CPU:**
_output_shapes
: *
pattern
^s3://.*Z
ConstConst"/device:CPU:**
_output_shapes
: *
dtype0*
valueB B.parta
Const_1Const"/device:CPU:**
_output_shapes
: *
dtype0*
valueB B
_temp/part�
SelectSelectStaticRegexFullMatch:output:0Const:output:0Const_1:output:0"/device:CPU:**
T0*
_output_shapes
: f

StringJoin
StringJoinfile_prefixSelect:output:0"/device:CPU:**
N*
_output_shapes
: n
Read/DisableCopyOnReadDisableCopyOnRead+read_disablecopyonread_vggish_conv1_weights*
_output_shapes
 �
Read/ReadVariableOpReadVariableOp+read_disablecopyonread_vggish_conv1_weights^Read/DisableCopyOnRead*&
_output_shapes
:@*
dtype0b
IdentityIdentityRead/ReadVariableOp:value:0*
T0*&
_output_shapes
:@i

Identity_1IdentityIdentity:output:0"/device:CPU:0*
T0*&
_output_shapes
:@q
Read_1/DisableCopyOnReadDisableCopyOnRead,read_1_disablecopyonread_vggish_conv1_biases*
_output_shapes
 �
Read_1/ReadVariableOpReadVariableOp,read_1_disablecopyonread_vggish_conv1_biases^Read_1/DisableCopyOnRead*
_output_shapes
:@*
dtype0Z

Identity_2IdentityRead_1/ReadVariableOp:value:0*
T0*
_output_shapes
:@_

Identity_3IdentityIdentity_2:output:0"/device:CPU:0*
T0*
_output_shapes
:@r
Read_2/DisableCopyOnReadDisableCopyOnRead-read_2_disablecopyonread_vggish_conv2_weights*
_output_shapes
 �
Read_2/ReadVariableOpReadVariableOp-read_2_disablecopyonread_vggish_conv2_weights^Read_2/DisableCopyOnRead*'
_output_shapes
:@�*
dtype0g

Identity_4IdentityRead_2/ReadVariableOp:value:0*
T0*'
_output_shapes
:@�l

Identity_5IdentityIdentity_4:output:0"/device:CPU:0*
T0*'
_output_shapes
:@�q
Read_3/DisableCopyOnReadDisableCopyOnRead,read_3_disablecopyonread_vggish_conv2_biases*
_output_shapes
 �
Read_3/ReadVariableOpReadVariableOp,read_3_disablecopyonread_vggish_conv2_biases^Read_3/DisableCopyOnRead*
_output_shapes	
:�*
dtype0[

Identity_6IdentityRead_3/ReadVariableOp:value:0*
T0*
_output_shapes	
:�`

Identity_7IdentityIdentity_6:output:0"/device:CPU:0*
T0*
_output_shapes	
:�z
Read_4/DisableCopyOnReadDisableCopyOnRead5read_4_disablecopyonread_vggish_conv3_conv3_1_weights*
_output_shapes
 �
Read_4/ReadVariableOpReadVariableOp5read_4_disablecopyonread_vggish_conv3_conv3_1_weights^Read_4/DisableCopyOnRead*(
_output_shapes
:��*
dtype0h

Identity_8IdentityRead_4/ReadVariableOp:value:0*
T0*(
_output_shapes
:��m

Identity_9IdentityIdentity_8:output:0"/device:CPU:0*
T0*(
_output_shapes
:��y
Read_5/DisableCopyOnReadDisableCopyOnRead4read_5_disablecopyonread_vggish_conv3_conv3_1_biases*
_output_shapes
 �
Read_5/ReadVariableOpReadVariableOp4read_5_disablecopyonread_vggish_conv3_conv3_1_biases^Read_5/DisableCopyOnRead*
_output_shapes	
:�*
dtype0\
Identity_10IdentityRead_5/ReadVariableOp:value:0*
T0*
_output_shapes	
:�b
Identity_11IdentityIdentity_10:output:0"/device:CPU:0*
T0*
_output_shapes	
:�z
Read_6/DisableCopyOnReadDisableCopyOnRead5read_6_disablecopyonread_vggish_conv3_conv3_2_weights*
_output_shapes
 �
Read_6/ReadVariableOpReadVariableOp5read_6_disablecopyonread_vggish_conv3_conv3_2_weights^Read_6/DisableCopyOnRead*(
_output_shapes
:��*
dtype0i
Identity_12IdentityRead_6/ReadVariableOp:value:0*
T0*(
_output_shapes
:��o
Identity_13IdentityIdentity_12:output:0"/device:CPU:0*
T0*(
_output_shapes
:��y
Read_7/DisableCopyOnReadDisableCopyOnRead4read_7_disablecopyonread_vggish_conv3_conv3_2_biases*
_output_shapes
 �
Read_7/ReadVariableOpReadVariableOp4read_7_disablecopyonread_vggish_conv3_conv3_2_biases^Read_7/DisableCopyOnRead*
_output_shapes	
:�*
dtype0\
Identity_14IdentityRead_7/ReadVariableOp:value:0*
T0*
_output_shapes	
:�b
Identity_15IdentityIdentity_14:output:0"/device:CPU:0*
T0*
_output_shapes	
:�z
Read_8/DisableCopyOnReadDisableCopyOnRead5read_8_disablecopyonread_vggish_conv4_conv4_1_weights*
_output_shapes
 �
Read_8/ReadVariableOpReadVariableOp5read_8_disablecopyonread_vggish_conv4_conv4_1_weights^Read_8/DisableCopyOnRead*(
_output_shapes
:��*
dtype0i
Identity_16IdentityRead_8/ReadVariableOp:value:0*
T0*(
_output_shapes
:��o
Identity_17IdentityIdentity_16:output:0"/device:CPU:0*
T0*(
_output_shapes
:��y
Read_9/DisableCopyOnReadDisableCopyOnRead4read_9_disablecopyonread_vggish_conv4_conv4_1_biases*
_output_shapes
 �
Read_9/ReadVariableOpReadVariableOp4read_9_disablecopyonread_vggish_conv4_conv4_1_biases^Read_9/DisableCopyOnRead*
_output_shapes	
:�*
dtype0\
Identity_18IdentityRead_9/ReadVariableOp:value:0*
T0*
_output_shapes	
:�b
Identity_19IdentityIdentity_18:output:0"/device:CPU:0*
T0*
_output_shapes	
:�|
Read_10/DisableCopyOnReadDisableCopyOnRead6read_10_disablecopyonread_vggish_conv4_conv4_2_weights*
_output_shapes
 �
Read_10/ReadVariableOpReadVariableOp6read_10_disablecopyonread_vggish_conv4_conv4_2_weights^Read_10/DisableCopyOnRead*(
_output_shapes
:��*
dtype0j
Identity_20IdentityRead_10/ReadVariableOp:value:0*
T0*(
_output_shapes
:��o
Identity_21IdentityIdentity_20:output:0"/device:CPU:0*
T0*(
_output_shapes
:��{
Read_11/DisableCopyOnReadDisableCopyOnRead5read_11_disablecopyonread_vggish_conv4_conv4_2_biases*
_output_shapes
 �
Read_11/ReadVariableOpReadVariableOp5read_11_disablecopyonread_vggish_conv4_conv4_2_biases^Read_11/DisableCopyOnRead*
_output_shapes	
:�*
dtype0]
Identity_22IdentityRead_11/ReadVariableOp:value:0*
T0*
_output_shapes	
:�b
Identity_23IdentityIdentity_22:output:0"/device:CPU:0*
T0*
_output_shapes	
:�x
Read_12/DisableCopyOnReadDisableCopyOnRead2read_12_disablecopyonread_vggish_fc1_fc1_1_weights*
_output_shapes
 �
Read_12/ReadVariableOpReadVariableOp2read_12_disablecopyonread_vggish_fc1_fc1_1_weights^Read_12/DisableCopyOnRead* 
_output_shapes
:
�`� *
dtype0b
Identity_24IdentityRead_12/ReadVariableOp:value:0*
T0* 
_output_shapes
:
�`� g
Identity_25IdentityIdentity_24:output:0"/device:CPU:0*
T0* 
_output_shapes
:
�`� w
Read_13/DisableCopyOnReadDisableCopyOnRead1read_13_disablecopyonread_vggish_fc1_fc1_1_biases*
_output_shapes
 �
Read_13/ReadVariableOpReadVariableOp1read_13_disablecopyonread_vggish_fc1_fc1_1_biases^Read_13/DisableCopyOnRead*
_output_shapes	
:� *
dtype0]
Identity_26IdentityRead_13/ReadVariableOp:value:0*
T0*
_output_shapes	
:� b
Identity_27IdentityIdentity_26:output:0"/device:CPU:0*
T0*
_output_shapes	
:� x
Read_14/DisableCopyOnReadDisableCopyOnRead2read_14_disablecopyonread_vggish_fc1_fc1_2_weights*
_output_shapes
 �
Read_14/ReadVariableOpReadVariableOp2read_14_disablecopyonread_vggish_fc1_fc1_2_weights^Read_14/DisableCopyOnRead* 
_output_shapes
:
� � *
dtype0b
Identity_28IdentityRead_14/ReadVariableOp:value:0*
T0* 
_output_shapes
:
� � g
Identity_29IdentityIdentity_28:output:0"/device:CPU:0*
T0* 
_output_shapes
:
� � w
Read_15/DisableCopyOnReadDisableCopyOnRead1read_15_disablecopyonread_vggish_fc1_fc1_2_biases*
_output_shapes
 �
Read_15/ReadVariableOpReadVariableOp1read_15_disablecopyonread_vggish_fc1_fc1_2_biases^Read_15/DisableCopyOnRead*
_output_shapes	
:� *
dtype0]
Identity_30IdentityRead_15/ReadVariableOp:value:0*
T0*
_output_shapes	
:� b
Identity_31IdentityIdentity_30:output:0"/device:CPU:0*
T0*
_output_shapes	
:� r
Read_16/DisableCopyOnReadDisableCopyOnRead,read_16_disablecopyonread_vggish_fc2_weights*
_output_shapes
 �
Read_16/ReadVariableOpReadVariableOp,read_16_disablecopyonread_vggish_fc2_weights^Read_16/DisableCopyOnRead* 
_output_shapes
:
� �*
dtype0b
Identity_32IdentityRead_16/ReadVariableOp:value:0*
T0* 
_output_shapes
:
� �g
Identity_33IdentityIdentity_32:output:0"/device:CPU:0*
T0* 
_output_shapes
:
� �q
Read_17/DisableCopyOnReadDisableCopyOnRead+read_17_disablecopyonread_vggish_fc2_biases*
_output_shapes
 �
Read_17/ReadVariableOpReadVariableOp+read_17_disablecopyonread_vggish_fc2_biases^Read_17/DisableCopyOnRead*
_output_shapes	
:�*
dtype0]
Identity_34IdentityRead_17/ReadVariableOp:value:0*
T0*
_output_shapes	
:�b
Identity_35IdentityIdentity_34:output:0"/device:CPU:0*
T0*
_output_shapes	
:�L

num_shardsConst*
_output_shapes
: *
dtype0*
value	B :f
ShardedFilename/shardConst"/device:CPU:0*
_output_shapes
: *
dtype0*
value	B : �
ShardedFilenameShardedFilenameStringJoin:output:0ShardedFilename/shard:output:0num_shards:output:0"/device:CPU:0*
_output_shapes
: �
SaveV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*�
value�B�B'_variables/0/.ATTRIBUTES/VARIABLE_VALUEB'_variables/1/.ATTRIBUTES/VARIABLE_VALUEB'_variables/2/.ATTRIBUTES/VARIABLE_VALUEB'_variables/3/.ATTRIBUTES/VARIABLE_VALUEB'_variables/4/.ATTRIBUTES/VARIABLE_VALUEB'_variables/5/.ATTRIBUTES/VARIABLE_VALUEB'_variables/6/.ATTRIBUTES/VARIABLE_VALUEB'_variables/7/.ATTRIBUTES/VARIABLE_VALUEB'_variables/8/.ATTRIBUTES/VARIABLE_VALUEB'_variables/9/.ATTRIBUTES/VARIABLE_VALUEB(_variables/10/.ATTRIBUTES/VARIABLE_VALUEB(_variables/11/.ATTRIBUTES/VARIABLE_VALUEB(_variables/12/.ATTRIBUTES/VARIABLE_VALUEB(_variables/13/.ATTRIBUTES/VARIABLE_VALUEB(_variables/14/.ATTRIBUTES/VARIABLE_VALUEB(_variables/15/.ATTRIBUTES/VARIABLE_VALUEB(_variables/16/.ATTRIBUTES/VARIABLE_VALUEB(_variables/17/.ATTRIBUTES/VARIABLE_VALUEB_CHECKPOINTABLE_OBJECT_GRAPH�
SaveV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*9
value0B.B B B B B B B B B B B B B B B B B B B �
SaveV2SaveV2ShardedFilename:filename:0SaveV2/tensor_names:output:0 SaveV2/shape_and_slices:output:0Identity_1:output:0Identity_3:output:0Identity_5:output:0Identity_7:output:0Identity_9:output:0Identity_11:output:0Identity_13:output:0Identity_15:output:0Identity_17:output:0Identity_19:output:0Identity_21:output:0Identity_23:output:0Identity_25:output:0Identity_27:output:0Identity_29:output:0Identity_31:output:0Identity_33:output:0Identity_35:output:0savev2_const"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *!
dtypes
2�
&MergeV2Checkpoints/checkpoint_prefixesPackShardedFilename:filename:0^SaveV2"/device:CPU:0*
N*
T0*
_output_shapes
:�
MergeV2CheckpointsMergeV2Checkpoints/MergeV2Checkpoints/checkpoint_prefixes:output:0file_prefix"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 i
Identity_36Identityfile_prefix^MergeV2Checkpoints"/device:CPU:0*
T0*
_output_shapes
: U
Identity_37IdentityIdentity_36:output:0^NoOp*
T0*
_output_shapes
: �
NoOpNoOp^MergeV2Checkpoints^Read/DisableCopyOnRead^Read/ReadVariableOp^Read_1/DisableCopyOnRead^Read_1/ReadVariableOp^Read_10/DisableCopyOnRead^Read_10/ReadVariableOp^Read_11/DisableCopyOnRead^Read_11/ReadVariableOp^Read_12/DisableCopyOnRead^Read_12/ReadVariableOp^Read_13/DisableCopyOnRead^Read_13/ReadVariableOp^Read_14/DisableCopyOnRead^Read_14/ReadVariableOp^Read_15/DisableCopyOnRead^Read_15/ReadVariableOp^Read_16/DisableCopyOnRead^Read_16/ReadVariableOp^Read_17/DisableCopyOnRead^Read_17/ReadVariableOp^Read_2/DisableCopyOnRead^Read_2/ReadVariableOp^Read_3/DisableCopyOnRead^Read_3/ReadVariableOp^Read_4/DisableCopyOnRead^Read_4/ReadVariableOp^Read_5/DisableCopyOnRead^Read_5/ReadVariableOp^Read_6/DisableCopyOnRead^Read_6/ReadVariableOp^Read_7/DisableCopyOnRead^Read_7/ReadVariableOp^Read_8/DisableCopyOnRead^Read_8/ReadVariableOp^Read_9/DisableCopyOnRead^Read_9/ReadVariableOp*
_output_shapes
 "#
identity_37Identity_37:output:0*(
_construction_contextkEagerRuntime*;
_input_shapes*
(: : : : : : : : : : : : : : : : : : : : 2(
MergeV2CheckpointsMergeV2Checkpoints20
Read/DisableCopyOnReadRead/DisableCopyOnRead2*
Read/ReadVariableOpRead/ReadVariableOp24
Read_1/DisableCopyOnReadRead_1/DisableCopyOnRead2.
Read_1/ReadVariableOpRead_1/ReadVariableOp26
Read_10/DisableCopyOnReadRead_10/DisableCopyOnRead20
Read_10/ReadVariableOpRead_10/ReadVariableOp26
Read_11/DisableCopyOnReadRead_11/DisableCopyOnRead20
Read_11/ReadVariableOpRead_11/ReadVariableOp26
Read_12/DisableCopyOnReadRead_12/DisableCopyOnRead20
Read_12/ReadVariableOpRead_12/ReadVariableOp26
Read_13/DisableCopyOnReadRead_13/DisableCopyOnRead20
Read_13/ReadVariableOpRead_13/ReadVariableOp26
Read_14/DisableCopyOnReadRead_14/DisableCopyOnRead20
Read_14/ReadVariableOpRead_14/ReadVariableOp26
Read_15/DisableCopyOnReadRead_15/DisableCopyOnRead20
Read_15/ReadVariableOpRead_15/ReadVariableOp26
Read_16/DisableCopyOnReadRead_16/DisableCopyOnRead20
Read_16/ReadVariableOpRead_16/ReadVariableOp26
Read_17/DisableCopyOnReadRead_17/DisableCopyOnRead20
Read_17/ReadVariableOpRead_17/ReadVariableOp24
Read_2/DisableCopyOnReadRead_2/DisableCopyOnRead2.
Read_2/ReadVariableOpRead_2/ReadVariableOp24
Read_3/DisableCopyOnReadRead_3/DisableCopyOnRead2.
Read_3/ReadVariableOpRead_3/ReadVariableOp24
Read_4/DisableCopyOnReadRead_4/DisableCopyOnRead2.
Read_4/ReadVariableOpRead_4/ReadVariableOp24
Read_5/DisableCopyOnReadRead_5/DisableCopyOnRead2.
Read_5/ReadVariableOpRead_5/ReadVariableOp24
Read_6/DisableCopyOnReadRead_6/DisableCopyOnRead2.
Read_6/ReadVariableOpRead_6/ReadVariableOp24
Read_7/DisableCopyOnReadRead_7/DisableCopyOnRead2.
Read_7/ReadVariableOpRead_7/ReadVariableOp24
Read_8/DisableCopyOnReadRead_8/DisableCopyOnRead2.
Read_8/ReadVariableOpRead_8/ReadVariableOp24
Read_9/DisableCopyOnReadRead_9/DisableCopyOnRead2.
Read_9/ReadVariableOpRead_9/ReadVariableOp:=9

_output_shapes
: 

_user_specified_nameConst:1-
+
_user_specified_namevggish/fc2/biases:2.
,
_user_specified_namevggish/fc2/weights:73
1
_user_specified_namevggish/fc1/fc1_2/biases:84
2
_user_specified_namevggish/fc1/fc1_2/weights:73
1
_user_specified_namevggish/fc1/fc1_1/biases:84
2
_user_specified_namevggish/fc1/fc1_1/weights:;7
5
_user_specified_namevggish/conv4/conv4_2/biases:<8
6
_user_specified_namevggish/conv4/conv4_2/weights:;
7
5
_user_specified_namevggish/conv4/conv4_1/biases:<	8
6
_user_specified_namevggish/conv4/conv4_1/weights:;7
5
_user_specified_namevggish/conv3/conv3_2/biases:<8
6
_user_specified_namevggish/conv3/conv3_2/weights:;7
5
_user_specified_namevggish/conv3/conv3_1/biases:<8
6
_user_specified_namevggish/conv3/conv3_1/weights:3/
-
_user_specified_namevggish/conv2/biases:40
.
_user_specified_namevggish/conv2/weights:3/
-
_user_specified_namevggish/conv1/biases:40
.
_user_specified_namevggish/conv1/weights:C ?

_output_shapes
: 
%
_user_specified_namefile_prefix
�X
�
__inference__traced_restore_990
file_prefix?
%assignvariableop_vggish_conv1_weights:@4
&assignvariableop_1_vggish_conv1_biases:@B
'assignvariableop_2_vggish_conv2_weights:@�5
&assignvariableop_3_vggish_conv2_biases:	�K
/assignvariableop_4_vggish_conv3_conv3_1_weights:��=
.assignvariableop_5_vggish_conv3_conv3_1_biases:	�K
/assignvariableop_6_vggish_conv3_conv3_2_weights:��=
.assignvariableop_7_vggish_conv3_conv3_2_biases:	�K
/assignvariableop_8_vggish_conv4_conv4_1_weights:��=
.assignvariableop_9_vggish_conv4_conv4_1_biases:	�L
0assignvariableop_10_vggish_conv4_conv4_2_weights:��>
/assignvariableop_11_vggish_conv4_conv4_2_biases:	�@
,assignvariableop_12_vggish_fc1_fc1_1_weights:
�`� :
+assignvariableop_13_vggish_fc1_fc1_1_biases:	� @
,assignvariableop_14_vggish_fc1_fc1_2_weights:
� � :
+assignvariableop_15_vggish_fc1_fc1_2_biases:	� :
&assignvariableop_16_vggish_fc2_weights:
� �4
%assignvariableop_17_vggish_fc2_biases:	�
identity_19��AssignVariableOp�AssignVariableOp_1�AssignVariableOp_10�AssignVariableOp_11�AssignVariableOp_12�AssignVariableOp_13�AssignVariableOp_14�AssignVariableOp_15�AssignVariableOp_16�AssignVariableOp_17�AssignVariableOp_2�AssignVariableOp_3�AssignVariableOp_4�AssignVariableOp_5�AssignVariableOp_6�AssignVariableOp_7�AssignVariableOp_8�AssignVariableOp_9�
RestoreV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*�
value�B�B'_variables/0/.ATTRIBUTES/VARIABLE_VALUEB'_variables/1/.ATTRIBUTES/VARIABLE_VALUEB'_variables/2/.ATTRIBUTES/VARIABLE_VALUEB'_variables/3/.ATTRIBUTES/VARIABLE_VALUEB'_variables/4/.ATTRIBUTES/VARIABLE_VALUEB'_variables/5/.ATTRIBUTES/VARIABLE_VALUEB'_variables/6/.ATTRIBUTES/VARIABLE_VALUEB'_variables/7/.ATTRIBUTES/VARIABLE_VALUEB'_variables/8/.ATTRIBUTES/VARIABLE_VALUEB'_variables/9/.ATTRIBUTES/VARIABLE_VALUEB(_variables/10/.ATTRIBUTES/VARIABLE_VALUEB(_variables/11/.ATTRIBUTES/VARIABLE_VALUEB(_variables/12/.ATTRIBUTES/VARIABLE_VALUEB(_variables/13/.ATTRIBUTES/VARIABLE_VALUEB(_variables/14/.ATTRIBUTES/VARIABLE_VALUEB(_variables/15/.ATTRIBUTES/VARIABLE_VALUEB(_variables/16/.ATTRIBUTES/VARIABLE_VALUEB(_variables/17/.ATTRIBUTES/VARIABLE_VALUEB_CHECKPOINTABLE_OBJECT_GRAPH�
RestoreV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*9
value0B.B B B B B B B B B B B B B B B B B B B �
	RestoreV2	RestoreV2file_prefixRestoreV2/tensor_names:output:0#RestoreV2/shape_and_slices:output:0"/device:CPU:0*`
_output_shapesN
L:::::::::::::::::::*!
dtypes
2[
IdentityIdentityRestoreV2:tensors:0"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOpAssignVariableOp%assignvariableop_vggish_conv1_weightsIdentity:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_1IdentityRestoreV2:tensors:1"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_1AssignVariableOp&assignvariableop_1_vggish_conv1_biasesIdentity_1:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_2IdentityRestoreV2:tensors:2"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_2AssignVariableOp'assignvariableop_2_vggish_conv2_weightsIdentity_2:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_3IdentityRestoreV2:tensors:3"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_3AssignVariableOp&assignvariableop_3_vggish_conv2_biasesIdentity_3:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_4IdentityRestoreV2:tensors:4"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_4AssignVariableOp/assignvariableop_4_vggish_conv3_conv3_1_weightsIdentity_4:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_5IdentityRestoreV2:tensors:5"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_5AssignVariableOp.assignvariableop_5_vggish_conv3_conv3_1_biasesIdentity_5:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_6IdentityRestoreV2:tensors:6"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_6AssignVariableOp/assignvariableop_6_vggish_conv3_conv3_2_weightsIdentity_6:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_7IdentityRestoreV2:tensors:7"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_7AssignVariableOp.assignvariableop_7_vggish_conv3_conv3_2_biasesIdentity_7:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_8IdentityRestoreV2:tensors:8"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_8AssignVariableOp/assignvariableop_8_vggish_conv4_conv4_1_weightsIdentity_8:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_9IdentityRestoreV2:tensors:9"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_9AssignVariableOp.assignvariableop_9_vggish_conv4_conv4_1_biasesIdentity_9:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0_
Identity_10IdentityRestoreV2:tensors:10"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_10AssignVariableOp0assignvariableop_10_vggish_conv4_conv4_2_weightsIdentity_10:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0_
Identity_11IdentityRestoreV2:tensors:11"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_11AssignVariableOp/assignvariableop_11_vggish_conv4_conv4_2_biasesIdentity_11:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0_
Identity_12IdentityRestoreV2:tensors:12"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_12AssignVariableOp,assignvariableop_12_vggish_fc1_fc1_1_weightsIdentity_12:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0_
Identity_13IdentityRestoreV2:tensors:13"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_13AssignVariableOp+assignvariableop_13_vggish_fc1_fc1_1_biasesIdentity_13:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0_
Identity_14IdentityRestoreV2:tensors:14"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_14AssignVariableOp,assignvariableop_14_vggish_fc1_fc1_2_weightsIdentity_14:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0_
Identity_15IdentityRestoreV2:tensors:15"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_15AssignVariableOp+assignvariableop_15_vggish_fc1_fc1_2_biasesIdentity_15:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0_
Identity_16IdentityRestoreV2:tensors:16"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_16AssignVariableOp&assignvariableop_16_vggish_fc2_weightsIdentity_16:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0_
Identity_17IdentityRestoreV2:tensors:17"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_17AssignVariableOp%assignvariableop_17_vggish_fc2_biasesIdentity_17:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0Y
NoOpNoOp"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 �
Identity_18Identityfile_prefix^AssignVariableOp^AssignVariableOp_1^AssignVariableOp_10^AssignVariableOp_11^AssignVariableOp_12^AssignVariableOp_13^AssignVariableOp_14^AssignVariableOp_15^AssignVariableOp_16^AssignVariableOp_17^AssignVariableOp_2^AssignVariableOp_3^AssignVariableOp_4^AssignVariableOp_5^AssignVariableOp_6^AssignVariableOp_7^AssignVariableOp_8^AssignVariableOp_9^NoOp"/device:CPU:0*
T0*
_output_shapes
: W
Identity_19IdentityIdentity_18:output:0^NoOp_1*
T0*
_output_shapes
: �
NoOp_1NoOp^AssignVariableOp^AssignVariableOp_1^AssignVariableOp_10^AssignVariableOp_11^AssignVariableOp_12^AssignVariableOp_13^AssignVariableOp_14^AssignVariableOp_15^AssignVariableOp_16^AssignVariableOp_17^AssignVariableOp_2^AssignVariableOp_3^AssignVariableOp_4^AssignVariableOp_5^AssignVariableOp_6^AssignVariableOp_7^AssignVariableOp_8^AssignVariableOp_9*
_output_shapes
 "#
identity_19Identity_19:output:0*(
_construction_contextkEagerRuntime*9
_input_shapes(
&: : : : : : : : : : : : : : : : : : : 2*
AssignVariableOp_10AssignVariableOp_102*
AssignVariableOp_11AssignVariableOp_112*
AssignVariableOp_12AssignVariableOp_122*
AssignVariableOp_13AssignVariableOp_132*
AssignVariableOp_14AssignVariableOp_142*
AssignVariableOp_15AssignVariableOp_152*
AssignVariableOp_16AssignVariableOp_162*
AssignVariableOp_17AssignVariableOp_172(
AssignVariableOp_1AssignVariableOp_12(
AssignVariableOp_2AssignVariableOp_22(
AssignVariableOp_3AssignVariableOp_32(
AssignVariableOp_4AssignVariableOp_42(
AssignVariableOp_5AssignVariableOp_52(
AssignVariableOp_6AssignVariableOp_62(
AssignVariableOp_7AssignVariableOp_72(
AssignVariableOp_8AssignVariableOp_82(
AssignVariableOp_9AssignVariableOp_92$
AssignVariableOpAssignVariableOp:1-
+
_user_specified_namevggish/fc2/biases:2.
,
_user_specified_namevggish/fc2/weights:73
1
_user_specified_namevggish/fc1/fc1_2/biases:84
2
_user_specified_namevggish/fc1/fc1_2/weights:73
1
_user_specified_namevggish/fc1/fc1_1/biases:84
2
_user_specified_namevggish/fc1/fc1_1/weights:;7
5
_user_specified_namevggish/conv4/conv4_2/biases:<8
6
_user_specified_namevggish/conv4/conv4_2/weights:;
7
5
_user_specified_namevggish/conv4/conv4_1/biases:<	8
6
_user_specified_namevggish/conv4/conv4_1/weights:;7
5
_user_specified_namevggish/conv3/conv3_2/biases:<8
6
_user_specified_namevggish/conv3/conv3_2/weights:;7
5
_user_specified_namevggish/conv3/conv3_1/biases:<8
6
_user_specified_namevggish/conv3/conv3_1/weights:3/
-
_user_specified_namevggish/conv2/biases:40
.
_user_specified_namevggish/conv2/weights:3/
-
_user_specified_namevggish/conv1/biases:40
.
_user_specified_namevggish/conv1/weights:C ?

_output_shapes
: 
%
_user_specified_namefile_prefix"�L
saver_filename:0StatefulPartitionedCall_1:0StatefulPartitionedCall_28"
saved_model_main_op

NoOp*>
__saved_model_init_op%#
__saved_model_init_op

NoOp*�
serving_default�
9
waveform-
serving_default_waveform:0���������=
output_01
StatefulPartitionedCall:0����������tensorflow/serving/predict:�
�

_variables

signatures
#_self_saveable_object_factories
__call__

_vggish_fn"
_generic_user_object
�
0
1
2
	3

4
5
6
7
8
9
10
11
12
13
14
15
16
17"
trackable_list_wrapper
,
serving_default"
signature_map
 "
trackable_dict_wrapper
�
trace_02�
__inference___call___503�
���
FullArgSpec
args�

jwaveform
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *�
����������ztrace_0
�B�
 __inference_wrapped_function_480"�
���
FullArgSpec
args�	
jarg_0
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *
 
,:*@2vggish/conv1/weights
:@2vggish/conv1/biases
-:+@�2vggish/conv2/weights
 :�2vggish/conv2/biases
6:4��2vggish/conv3/conv3_1/weights
(:&�2vggish/conv3/conv3_1/biases
6:4��2vggish/conv3/conv3_2/weights
(:&�2vggish/conv3/conv3_2/biases
6:4��2vggish/conv4/conv4_1/weights
(:&�2vggish/conv4/conv4_1/biases
6:4��2vggish/conv4/conv4_2/weights
(:&�2vggish/conv4/conv4_2/biases
*:(
�`� 2vggish/fc1/fc1_1/weights
$:"� 2vggish/fc1/fc1_1/biases
*:(
� � 2vggish/fc1/fc1_2/weights
$:"� 2vggish/fc1/fc1_2/biases
$:"
� �2vggish/fc2/weights
:�2vggish/fc2/biases
�B�
!__inference_signature_wrapper_797waveform"�
���
FullArgSpec
args� 
varargs
 
varkw
 
defaults
 

kwonlyargs�

jwaveform
kwonlydefaults
 
annotations� *
 
�B�
__inference___call___503"�
���
FullArgSpec
args�

jwaveform
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *
 z
__inference___call___503^	
-�*
#� 
�
waveform���������
� "������������
!__inference_signature_wrapper_797�	
9�6
� 
/�,
*
waveform�
waveform���������"4�1
/
output_0#� 
output_0����������{
 __inference_wrapped_function_480W	
&�#
�
�
0���������
� "�����������