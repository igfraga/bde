# bsl

list(APPEND sources
    "bslalg/bslalg_arraydestructionprimitives.cpp"
    "bslalg/bslalg_arraydestructionprimitives.h"
    "bslalg/bslalg_arrayprimitives.cpp"
    "bslalg/bslalg_arrayprimitives.h"
    "bslalg/bslalg_autoarraydestructor.cpp"
    "bslalg/bslalg_autoarraydestructor.h"
    "bslalg/bslalg_autoarraymovedestructor.cpp"
    "bslalg/bslalg_autoarraymovedestructor.h"
    "bslalg/bslalg_autoscalardestructor.cpp"
    "bslalg/bslalg_autoscalardestructor.h"
    "bslalg/bslalg_bidirectionallink.cpp"
    "bslalg/bslalg_bidirectionallink.h"
    "bslalg/bslalg_bidirectionalnode.cpp"
    "bslalg/bslalg_bidirectionalnode.h"
    "bslalg/bslalg_bidirectionallinklistutil.cpp"
    "bslalg/bslalg_bidirectionallinklistutil.h"
    "bslalg/bslalg_constructorproxy.cpp"
    "bslalg/bslalg_constructorproxy.h"
    "bslalg/bslalg_containerbase.cpp"
    "bslalg/bslalg_containerbase.h"
    "bslalg/bslalg_dequeimputil.cpp"
    "bslalg/bslalg_dequeimputil.h"
    "bslalg/bslalg_dequeiterator.cpp"
    "bslalg/bslalg_dequeiterator.h"
    "bslalg/bslalg_dequeprimitives.cpp"
    "bslalg/bslalg_dequeprimitives.h"
    "bslalg/bslalg_functoradapter.cpp"
    "bslalg/bslalg_functoradapter.h"
    "bslalg/bslalg_hashtableanchor.cpp"
    "bslalg/bslalg_hashtableanchor.h"
    "bslalg/bslalg_hashtablebucket.cpp"
    "bslalg/bslalg_hashtablebucket.h"
    "bslalg/bslalg_hashtableimputil.cpp"
    "bslalg/bslalg_hashtableimputil.h"
    "bslalg/bslalg_hashutil.cpp"
    "bslalg/bslalg_hashutil.h"
    "bslalg/bslalg_hasstliterators.cpp"
    "bslalg/bslalg_hasstliterators.h"
    "bslalg/bslalg_hastrait.cpp"
    "bslalg/bslalg_hastrait.h"
    "bslalg/bslalg_rangecompare.cpp"
    "bslalg/bslalg_rangecompare.h"
    "bslalg/bslalg_rbtreeanchor.cpp"
    "bslalg/bslalg_rbtreeanchor.h"
    "bslalg/bslalg_rbtreenode.cpp"
    "bslalg/bslalg_rbtreenode.h"
    "bslalg/bslalg_rbtreeutil.cpp"
    "bslalg/bslalg_rbtreeutil.h"
    "bslalg/bslalg_scalardestructionprimitives.cpp"
    "bslalg/bslalg_scalardestructionprimitives.h"
    "bslalg/bslalg_scalarprimitives.cpp"
    "bslalg/bslalg_scalarprimitives.h"
    "bslalg/bslalg_selecttrait.cpp"
    "bslalg/bslalg_selecttrait.h"
    "bslalg/bslalg_swaputil.cpp"
    "bslalg/bslalg_swaputil.h"
    "bslalg/bslalg_typetraitbitwisecopyable.cpp"
    "bslalg/bslalg_typetraitbitwisecopyable.h"
    "bslalg/bslalg_typetraitbitwiseequalitycomparable.cpp"
    "bslalg/bslalg_typetraitbitwiseequalitycomparable.h"
    "bslalg/bslalg_typetraitbitwisemoveable.cpp"
    "bslalg/bslalg_typetraitbitwisemoveable.h"
    "bslalg/bslalg_typetraithaspointersemantics.cpp"
    "bslalg/bslalg_typetraithaspointersemantics.h"
    "bslalg/bslalg_typetraithasstliterators.cpp"
    "bslalg/bslalg_typetraithasstliterators.h"
    "bslalg/bslalg_typetraithastrivialdefaultconstructor.cpp"
    "bslalg/bslalg_typetraithastrivialdefaultconstructor.h"
    "bslalg/bslalg_typetraitnil.cpp"
    "bslalg/bslalg_typetraitnil.h"
    "bslalg/bslalg_typetraitpair.cpp"
    "bslalg/bslalg_typetraitpair.h"
    "bslalg/bslalg_typetraits.cpp"
    "bslalg/bslalg_typetraits.h"
    "bslalg/bslalg_typetraitusesbslmaallocator.cpp"
    "bslalg/bslalg_typetraitusesbslmaallocator.h"
    "bsldoc/bsldoc_glossary.cpp"
    "bsldoc/bsldoc_glossary.h"
    "bslh/bslh_defaulthashalgorithm.cpp"
    "bslh/bslh_defaulthashalgorithm.h"
    "bslh/bslh_defaultseededhashalgorithm.cpp"
    "bslh/bslh_defaultseededhashalgorithm.h"
    "bslh/bslh_hash.cpp"
    "bslh/bslh_hash.h"
    "bslh/bslh_seededhash.cpp"
    "bslh/bslh_seededhash.h"
    "bslh/bslh_seedgenerator.cpp"
    "bslh/bslh_seedgenerator.h"
    "bslh/bslh_siphashalgorithm.cpp"
    "bslh/bslh_siphashalgorithm.h"
    "bslh/bslh_spookyhashalgorithm.cpp"
    "bslh/bslh_spookyhashalgorithm.h"
    "bslh/bslh_spookyhashalgorithmimp.cpp"
    "bslh/bslh_spookyhashalgorithmimp.h"
    "bslim/bslim_printer.cpp"
    "bslim/bslim_printer.h"
    "bslim/bslim_testutil.cpp"
    "bslim/bslim_testutil.h"
    "bslma/bslma_allocator.cpp"
    "bslma/bslma_allocator.h"
    "bslma/bslma_allocatoradaptor.cpp"
    "bslma/bslma_allocatoradaptor.h"
    "bslma/bslma_allocatortraits.cpp"
    "bslma/bslma_allocatortraits.h"
    "bslma/bslma_autodeallocator.cpp"
    "bslma/bslma_autodeallocator.h"
    "bslma/bslma_autodestructor.cpp"
    "bslma/bslma_autodestructor.h"
    "bslma/bslma_autorawdeleter.cpp"
    "bslma/bslma_autorawdeleter.h"
    "bslma/bslma_constructionutil.cpp"
    "bslma/bslma_constructionutil.h"
    "bslma/bslma_deallocatorguard.cpp"
    "bslma/bslma_deallocatorguard.h"
    "bslma/bslma_deallocatorproctor.cpp"
    "bslma/bslma_deallocatorproctor.h"
    "bslma/bslma_default.cpp"
    "bslma/bslma_default.h"
    "bslma/bslma_defaultallocatorguard.cpp"
    "bslma/bslma_defaultallocatorguard.h"
    "bslma/bslma_deleterhelper.cpp"
    "bslma/bslma_deleterhelper.h"
    "bslma/bslma_destructionutil.cpp"
    "bslma/bslma_destructionutil.h"
    "bslma/bslma_destructorguard.cpp"
    "bslma/bslma_destructorguard.h"
    "bslma/bslma_destructorproctor.cpp"
    "bslma/bslma_destructorproctor.h"
    "bslma/bslma_exceptionguard.cpp"
    "bslma/bslma_exceptionguard.h"
    "bslma/bslma_mallocfreeallocator.cpp"
    "bslma/bslma_mallocfreeallocator.h"
    "bslma/bslma_managedptr.cpp"
    "bslma/bslma_managedptr.h"
    "bslma/bslma_managedptr_factorydeleter.cpp"
    "bslma/bslma_managedptr_factorydeleter.h"
    "bslma/bslma_managedptr_members.cpp"
    "bslma/bslma_managedptr_members.h"
    "bslma/bslma_managedptr_pairproxy.cpp"
    "bslma/bslma_managedptr_pairproxy.h"
    "bslma/bslma_managedptrdeleter.cpp"
    "bslma/bslma_managedptrdeleter.h"
    "bslma/bslma_newdeleteallocator.cpp"
    "bslma/bslma_newdeleteallocator.h"
    "bslma/bslma_rawdeleterguard.cpp"
    "bslma/bslma_rawdeleterguard.h"
    "bslma/bslma_rawdeleterproctor.cpp"
    "bslma/bslma_rawdeleterproctor.h"
    "bslma/bslma_sharedptrinplacerep.cpp"
    "bslma/bslma_sharedptrinplacerep.h"
    "bslma/bslma_sharedptroutofplacerep.cpp"
    "bslma/bslma_sharedptroutofplacerep.h"
    "bslma/bslma_sharedptrrep.cpp"
    "bslma/bslma_sharedptrrep.h"
    "bslma/bslma_stdallocator.cpp"
    "bslma/bslma_stdallocator.h"
    "bslma/bslma_stdtestallocator.cpp"
    "bslma/bslma_stdtestallocator.h"
    "bslma/bslma_testallocator.cpp"
    "bslma/bslma_testallocator.h"
    "bslma/bslma_testallocatorexception.cpp"
    "bslma/bslma_testallocatorexception.h"
    "bslma/bslma_testallocatormonitor.cpp"
    "bslma/bslma_testallocatormonitor.h"
    "bslma/bslma_usesbslmaallocator.cpp"
    "bslma/bslma_usesbslmaallocator.h"
    "bslmf/bslmf_addconst.cpp"
    "bslmf/bslmf_addconst.h"
    "bslmf/bslmf_addcv.cpp"
    "bslmf/bslmf_addcv.h"
    "bslmf/bslmf_addpointer.cpp"
    "bslmf/bslmf_addpointer.h"
    "bslmf/bslmf_addlvaluereference.cpp"
    "bslmf/bslmf_addlvaluereference.h"
    "bslmf/bslmf_addreference.cpp"
    "bslmf/bslmf_addreference.h"
    "bslmf/bslmf_addrvaluereference.cpp"
    "bslmf/bslmf_addrvaluereference.h"
    "bslmf/bslmf_addvolatile.cpp"
    "bslmf/bslmf_addvolatile.h"
    "bslmf/bslmf_allocatorargt.cpp"
    "bslmf/bslmf_allocatorargt.h"
    "bslmf/bslmf_arraytopointer.cpp"
    "bslmf/bslmf_arraytopointer.h"
    "bslmf/bslmf_assert.cpp"
    "bslmf/bslmf_assert.h"
    "bslmf/bslmf_conditional.cpp"
    "bslmf/bslmf_conditional.h"
    "bslmf/bslmf_decay.cpp"
    "bslmf/bslmf_decay.h"
    "bslmf/bslmf_detectnestedtrait.cpp"
    "bslmf/bslmf_detectnestedtrait.h"
    "bslmf/bslmf_enableif.cpp"
    "bslmf/bslmf_enableif.h"
    "bslmf/bslmf_forwardingtype.cpp"
    "bslmf/bslmf_forwardingtype.h"
    "bslmf/bslmf_functionpointertraits.cpp"
    "bslmf/bslmf_functionpointertraits.h"
    "bslmf/bslmf_haspointersemantics.cpp"
    "bslmf/bslmf_haspointersemantics.h"
    "bslmf/bslmf_if.cpp"
    "bslmf/bslmf_if.h"
    "bslmf/bslmf_integralconstant.cpp"
    "bslmf/bslmf_integralconstant.h"
    "bslmf/bslmf_isarithmetic.cpp"
    "bslmf/bslmf_isarithmetic.h"
    "bslmf/bslmf_isarray.cpp"
    "bslmf/bslmf_isarray.h"
    "bslmf/bslmf_isbitwiseequalitycomparable.cpp"
    "bslmf/bslmf_isbitwiseequalitycomparable.h"
    "bslmf/bslmf_isbitwisemoveable.cpp"
    "bslmf/bslmf_isbitwisemoveable.h"
    "bslmf/bslmf_isclass.cpp"
    "bslmf/bslmf_isclass.h"
    "bslmf/bslmf_isconst.cpp"
    "bslmf/bslmf_isconst.h"
    "bslmf/bslmf_isconvertible.cpp"
    "bslmf/bslmf_isconvertible.h"
    "bslmf/bslmf_isconvertibletoany.cpp"
    "bslmf/bslmf_isconvertibletoany.h"
    "bslmf/bslmf_iscopyconstructible.cpp"
    "bslmf/bslmf_iscopyconstructible.h"
    "bslmf/bslmf_isempty.cpp"
    "bslmf/bslmf_isempty.h"
    "bslmf/bslmf_isenum.cpp"
    "bslmf/bslmf_isenum.h"
    "bslmf/bslmf_isfloatingpoint.cpp"
    "bslmf/bslmf_isfloatingpoint.h"
    "bslmf/bslmf_isfunction.cpp"
    "bslmf/bslmf_isfunction.h"
    "bslmf/bslmf_isfundamental.cpp"
    "bslmf/bslmf_isfundamental.h"
    "bslmf/bslmf_isintegral.cpp"
    "bslmf/bslmf_isintegral.h"
    "bslmf/bslmf_islvaluereference.cpp"
    "bslmf/bslmf_islvaluereference.h"
    "bslmf/bslmf_ismemberfunctionpointer.cpp"
    "bslmf/bslmf_ismemberfunctionpointer.h"
    "bslmf/bslmf_ismemberobjectpointer.cpp"
    "bslmf/bslmf_ismemberobjectpointer.h"
    "bslmf/bslmf_ismemberpointer.cpp"
    "bslmf/bslmf_ismemberpointer.h"
    "bslmf/bslmf_isnothrowmoveconstructible.cpp"
    "bslmf/bslmf_isnothrowmoveconstructible.h"
    "bslmf/bslmf_ispair.cpp"
    "bslmf/bslmf_ispair.h"
    "bslmf/bslmf_ispointer.cpp"
    "bslmf/bslmf_ispointer.h"
    "bslmf/bslmf_ispointertomember.cpp"
    "bslmf/bslmf_ispointertomember.h"
    "bslmf/bslmf_ispolymorphic.cpp"
    "bslmf/bslmf_ispolymorphic.h"
    "bslmf/bslmf_isreference.cpp"
    "bslmf/bslmf_isreference.h"
    "bslmf/bslmf_isrvaluereference.cpp"
    "bslmf/bslmf_isrvaluereference.h"
    "bslmf/bslmf_issame.cpp"
    "bslmf/bslmf_issame.h"
    "bslmf/bslmf_istriviallycopyable.cpp"
    "bslmf/bslmf_istriviallycopyable.h"
    "bslmf/bslmf_istriviallydefaultconstructible.cpp"
    "bslmf/bslmf_istriviallydefaultconstructible.h"
    "bslmf/bslmf_isvoid.cpp"
    "bslmf/bslmf_isvoid.h"
    "bslmf/bslmf_isvolatile.cpp"
    "bslmf/bslmf_isvolatile.h"
    "bslmf/bslmf_matchanytype.cpp"
    "bslmf/bslmf_matchanytype.h"
    "bslmf/bslmf_matcharithmetictype.cpp"
    "bslmf/bslmf_matcharithmetictype.h"
    "bslmf/bslmf_memberfunctionpointertraits.cpp"
    "bslmf/bslmf_memberfunctionpointertraits.h"
    "bslmf/bslmf_metaint.cpp"
    "bslmf/bslmf_metaint.h"
    "bslmf/bslmf_movableref.cpp"
    "bslmf/bslmf_movableref.h"
    "bslmf/bslmf_nestedtraitdeclaration.cpp"
    "bslmf/bslmf_nestedtraitdeclaration.h"
    "bslmf/bslmf_nil.cpp"
    "bslmf/bslmf_nil.h"
    "bslmf/bslmf_nthparameter.cpp"
    "bslmf/bslmf_nthparameter.h"
    "bslmf/bslmf_removeconst.cpp"
    "bslmf/bslmf_removeconst.h"
    "bslmf/bslmf_removecv.cpp"
    "bslmf/bslmf_removecv.h"
    "bslmf/bslmf_removecvq.cpp"
    "bslmf/bslmf_removecvq.h"
    "bslmf/bslmf_removeextent.cpp"
    "bslmf/bslmf_removeextent.h"
    "bslmf/bslmf_removepointer.cpp"
    "bslmf/bslmf_removepointer.h"
    "bslmf/bslmf_removereference.cpp"
    "bslmf/bslmf_removereference.h"
    "bslmf/bslmf_removevolatile.cpp"
    "bslmf/bslmf_removevolatile.h"
    "bslmf/bslmf_resulttype.cpp"
    "bslmf/bslmf_resulttype.h"
    "bslmf/bslmf_switch.cpp"
    "bslmf/bslmf_switch.h"
    "bslmf/bslmf_selecttrait.cpp"
    "bslmf/bslmf_selecttrait.h"
    "bslmf/bslmf_tag.cpp"
    "bslmf/bslmf_tag.h"
    "bslmf/bslmf_typelist.cpp"
    "bslmf/bslmf_typelist.h"
    "bslmf/bslmf_usesallocator.cpp"
    "bslmf/bslmf_usesallocator.h"
    "bslmf/bslmf_usesallocatorargt.cpp"
    "bslmf/bslmf_usesallocatorargt.h"
    "bslmf/bslmf_util.cpp"
    "bslmf/bslmf_util.h"
    "bslmf/bslmf_voidtype.cpp"
    "bslmf/bslmf_voidtype.h"
    "bslmt/bslmt_barrier.cpp"
    "bslmt/bslmt_barrier.h"
    "bslmt/bslmt_condition.cpp"
    "bslmt/bslmt_condition.h"
    "bslmt/bslmt_conditionimpl_pthread.cpp"
    "bslmt/bslmt_conditionimpl_pthread.h"
    "bslmt/bslmt_conditionimpl_win32.cpp"
    "bslmt/bslmt_conditionimpl_win32.h"
    "bslmt/bslmt_configuration.cpp"
    "bslmt/bslmt_configuration.h"
    "bslmt/bslmt_entrypointfunctoradapter.cpp"
    "bslmt/bslmt_entrypointfunctoradapter.h"
    "bslmt/bslmt_latch.cpp"
    "bslmt/bslmt_latch.h"
    "bslmt/bslmt_lockguard.cpp"
    "bslmt/bslmt_lockguard.h"
    "bslmt/bslmt_meteredmutex.cpp"
    "bslmt/bslmt_meteredmutex.h"
    "bslmt/bslmt_mutex.cpp"
    "bslmt/bslmt_mutex.h"
    "bslmt/bslmt_mutexassert.cpp"
    "bslmt/bslmt_mutexassert.h"
    "bslmt/bslmt_muteximpl_pthread.cpp"
    "bslmt/bslmt_muteximpl_pthread.h"
    "bslmt/bslmt_muteximpl_win32.cpp"
    "bslmt/bslmt_muteximpl_win32.h"
    "bslmt/bslmt_once.cpp"
    "bslmt/bslmt_once.h"
    "bslmt/bslmt_platform.cpp"
    "bslmt/bslmt_platform.h"
    "bslmt/bslmt_qlock.cpp"
    "bslmt/bslmt_qlock.h"
    "bslmt/bslmt_readerwriterlock.cpp"
    "bslmt/bslmt_readerwriterlock.h"
    "bslmt/bslmt_readerwritermutex.cpp"
    "bslmt/bslmt_readerwritermutex.h"
    "bslmt/bslmt_readerwritermuteximpl.cpp"
    "bslmt/bslmt_readerwritermuteximpl.h"
    "bslmt/bslmt_readlockguard.cpp"
    "bslmt/bslmt_readlockguard.h"
    "bslmt/bslmt_recursivemutex.cpp"
    "bslmt/bslmt_recursivemutex.h"
    "bslmt/bslmt_recursivemuteximpl_pthread.cpp"
    "bslmt/bslmt_recursivemuteximpl_pthread.h"
    "bslmt/bslmt_recursivemuteximpl_win32.cpp"
    "bslmt/bslmt_recursivemuteximpl_win32.h"
    "bslmt/bslmt_rwmutex.cpp"
    "bslmt/bslmt_rwmutex.h"
    "bslmt/bslmt_saturatedtimeconversionimputil.cpp"
    "bslmt/bslmt_saturatedtimeconversionimputil.h"
    "bslmt/bslmt_semaphore.cpp"
    "bslmt/bslmt_semaphore.h"
    "bslmt/bslmt_semaphoreimpl_counted.cpp"
    "bslmt/bslmt_semaphoreimpl_counted.h"
    "bslmt/bslmt_semaphoreimpl_darwin.cpp"
    "bslmt/bslmt_semaphoreimpl_darwin.h"
    "bslmt/bslmt_semaphoreimpl_pthread.cpp"
    "bslmt/bslmt_semaphoreimpl_pthread.h"
    "bslmt/bslmt_semaphoreimpl_win32.cpp"
    "bslmt/bslmt_semaphoreimpl_win32.h"
    "bslmt/bslmt_sluice.cpp"
    "bslmt/bslmt_sluice.h"
    "bslmt/bslmt_threadattributes.cpp"
    "bslmt/bslmt_threadattributes.h"
    "bslmt/bslmt_threadgroup.cpp"
    "bslmt/bslmt_threadgroup.h"
    "bslmt/bslmt_threadlocalvariable.cpp"
    "bslmt/bslmt_threadlocalvariable.h"
    "bslmt/bslmt_threadutil.cpp"
    "bslmt/bslmt_threadutil.h"
    "bslmt/bslmt_threadutilimpl_pthread.cpp"
    "bslmt/bslmt_threadutilimpl_pthread.h"
    "bslmt/bslmt_threadutilimpl_win32.cpp"
    "bslmt/bslmt_threadutilimpl_win32.h"
    "bslmt/bslmt_timedsemaphore.cpp"
    "bslmt/bslmt_timedsemaphore.h"
    "bslmt/bslmt_timedsemaphoreimpl_posixadv.cpp"
    "bslmt/bslmt_timedsemaphoreimpl_posixadv.h"
    "bslmt/bslmt_timedsemaphoreimpl_pthread.cpp"
    "bslmt/bslmt_timedsemaphoreimpl_pthread.h"
    "bslmt/bslmt_timedsemaphoreimpl_win32.cpp"
    "bslmt/bslmt_timedsemaphoreimpl_win32.h"
    "bslmt/bslmt_turnstile.cpp"
    "bslmt/bslmt_turnstile.h"
    "bslmt/bslmt_writelockguard.cpp"
    "bslmt/bslmt_writelockguard.h"
    "bsls/bsls_alignedbuffer.cpp"
    "bsls/bsls_alignedbuffer.h"
    "bsls/bsls_alignment.cpp"
    "bsls/bsls_alignment.h"
    "bsls/bsls_alignmentfromtype.cpp"
    "bsls/bsls_alignmentfromtype.h"
    "bsls/bsls_alignmentimp.cpp"
    "bsls/bsls_alignmentimp.h"
    "bsls/bsls_alignmenttotype.cpp"
    "bsls/bsls_alignmenttotype.h"
    "bsls/bsls_alignmentutil.cpp"
    "bsls/bsls_alignmentutil.h"
    "bsls/bsls_annotation.cpp"
    "bsls/bsls_annotation.h"
    "bsls/bsls_assert.cpp"
    "bsls/bsls_assert.h"
    "bsls/bsls_asserttest.cpp"
    "bsls/bsls_asserttest.h"
    "bsls/bsls_asserttestexception.cpp"
    "bsls/bsls_asserttestexception.h"
    "bsls/bsls_atomic.cpp"
    "bsls/bsls_atomic.h"
    "bsls/bsls_atomicoperations.cpp"
    "bsls/bsls_atomicoperations.h"
    "bsls/bsls_atomicoperations_all_all_clangintrinsics.cpp"
    "bsls/bsls_atomicoperations_all_all_clangintrinsics.h"
    "bsls/bsls_atomicoperations_all_all_gccintrinsics.cpp"
    "bsls/bsls_atomicoperations_all_all_gccintrinsics.h"
    "bsls/bsls_atomicoperations_arm_all_gcc.cpp"
    "bsls/bsls_atomicoperations_arm_all_gcc.h"
    "bsls/bsls_atomicoperations_default.cpp"
    "bsls/bsls_atomicoperations_default.h"
    "bsls/bsls_atomicoperations_ia64_hp_acc.cpp"
    "bsls/bsls_atomicoperations_ia64_hp_acc.h"
    "bsls/bsls_atomicoperations_powerpc32_aix_xlc.cpp"
    "bsls/bsls_atomicoperations_powerpc32_aix_xlc.h"
    "bsls/bsls_atomicoperations_powerpc64_aix_xlc.cpp"
    "bsls/bsls_atomicoperations_powerpc64_aix_xlc.h"
    "bsls/bsls_atomicoperations_powerpc_aix_xlc_default.cpp"
    "bsls/bsls_atomicoperations_powerpc_aix_xlc_default.h"
    "bsls/bsls_atomicoperations_powerpc_all_gcc.cpp"
    "bsls/bsls_atomicoperations_powerpc_all_gcc.h"
    "bsls/bsls_atomicoperations_sparc32_sun_cc.cpp"
    "bsls/bsls_atomicoperations_sparc32_sun_cc.h"
    "bsls/bsls_atomicoperations_sparc64_sun_cc.cpp"
    "bsls/bsls_atomicoperations_sparc64_sun_cc.h"
    "bsls/bsls_atomicoperations_sparc_sun_cc_default.cpp"
    "bsls/bsls_atomicoperations_sparc_sun_cc_default.h"
    "bsls/bsls_atomicoperations_x64_all_gcc.cpp"
    "bsls/bsls_atomicoperations_x64_all_gcc.h"
    "bsls/bsls_atomicoperations_x64_win_msvc.cpp"
    "bsls/bsls_atomicoperations_x64_win_msvc.h"
    "bsls/bsls_atomicoperations_x86_all_gcc.cpp"
    "bsls/bsls_atomicoperations_x86_all_gcc.h"
    "bsls/bsls_atomicoperations_x86_win_msvc.cpp"
    "bsls/bsls_atomicoperations_x86_win_msvc.h"
    "bsls/bsls_blockgrowth.cpp"
    "bsls/bsls_blockgrowth.h"
    "bsls/bsls_bslexceptionutil.cpp"
    "bsls/bsls_bslexceptionutil.h"
    "bsls/bsls_bsllock.cpp"
    "bsls/bsls_bsllock.h"
    "bsls/bsls_bslonce.cpp"
    "bsls/bsls_bslonce.h"
    "bsls/bsls_bsltestutil.cpp"
    "bsls/bsls_bsltestutil.h"
    "bsls/bsls_buildtarget.cpp"
    "bsls/bsls_buildtarget.h"
    "bsls/bsls_byteorder.cpp"
    "bsls/bsls_byteorder.h"
    "bsls/bsls_byteorderutil.cpp"
    "bsls/bsls_byteorderutil.h"
    "bsls/bsls_byteorderutil_impl.cpp"
    "bsls/bsls_byteorderutil_impl.h"
    "bsls/bsls_compilerfeatures.cpp"
    "bsls/bsls_compilerfeatures.h"
    "bsls/bsls_cpp11.cpp"
    "bsls/bsls_cpp11.h"
    "bsls/bsls_exceptionutil.cpp"
    "bsls/bsls_exceptionutil.h"
    "bsls/bsls_ident.cpp"
    "bsls/bsls_ident.h"
    "bsls/bsls_linkcoercion.cpp"
    "bsls/bsls_linkcoercion.h"
    "bsls/bsls_log.cpp"
    "bsls/bsls_log.h"
    "bsls/bsls_logseverity.cpp"
    "bsls/bsls_logseverity.h"
    "bsls/bsls_macroincrement.cpp"
    "bsls/bsls_macroincrement.h"
    "bsls/bsls_macrorepeat.cpp"
    "bsls/bsls_macrorepeat.h"
    "bsls/bsls_nameof.cpp"
    "bsls/bsls_nameof.h"
    "bsls/bsls_nativestd.cpp"
    "bsls/bsls_nativestd.h"
    "bsls/bsls_nullptr.cpp"
    "bsls/bsls_nullptr.h"
    "bsls/bsls_objectbuffer.cpp"
    "bsls/bsls_objectbuffer.h"
    "bsls/bsls_performancehint.cpp"
    "bsls/bsls_performancehint.h"
    "bsls/bsls_platform.cpp"
    "bsls/bsls_platform.h"
    "bsls/bsls_pointercastutil.cpp"
    "bsls/bsls_pointercastutil.h"
    "bsls/bsls_protocoltest.cpp"
    "bsls/bsls_protocoltest.h"
    "bsls/bsls_spinlock.cpp"
    "bsls/bsls_spinlock.h"
    "bsls/bsls_stopwatch.cpp"
    "bsls/bsls_stopwatch.h"
    "bsls/bsls_systemclocktype.cpp"
    "bsls/bsls_systemclocktype.h"
    "bsls/bsls_systemtime.cpp"
    "bsls/bsls_systemtime.h"
    "bsls/bsls_timeinterval.cpp"
    "bsls/bsls_timeinterval.h"
    "bsls/bsls_timeutil.cpp"
    "bsls/bsls_timeutil.h"
    "bsls/bsls_types.cpp"
    "bsls/bsls_types.h"
    "bsls/bsls_unspecifiedbool.cpp"
    "bsls/bsls_unspecifiedbool.h"
    "bsls/bsls_util.cpp"
    "bsls/bsls_util.h"
    "bslscm/bslscm_patchversion.cpp"
    "bslscm/bslscm_patchversion.h"
    "bslscm/bslscm_version.cpp"
    "bslscm/bslscm_version.h"
    "bslscm/bslscm_versiontag.cpp"
    "bslscm/bslscm_versiontag.h"
    "bslstl/bslstl_algorithmworkaround.cpp"
    "bslstl/bslstl_algorithmworkaround.h"
    "bslstl/bslstl_allocator.cpp"
    "bslstl/bslstl_allocator.h"
    "bslstl/bslstl_allocatortraits.cpp"
    "bslstl/bslstl_allocatortraits.h"
    "bslstl/bslstl_badweakptr.cpp"
    "bslstl/bslstl_badweakptr.h"
    "bslstl/bslstl_bidirectionaliterator.cpp"
    "bslstl/bslstl_bidirectionaliterator.h"
    "bslstl/bslstl_bidirectionalnodepool.cpp"
    "bslstl/bslstl_bidirectionalnodepool.h"
    "bslstl/bslstl_bitset.cpp"
    "bslstl/bslstl_bitset.h"
    "bslstl/bslstl_deque.cpp"
    "bslstl/bslstl_deque.h"
    "bslstl/bslstl_equalto.cpp"
    "bslstl/bslstl_equalto.h"
    "bslstl/bslstl_forwarditerator.cpp"
    "bslstl/bslstl_forwarditerator.h"
    "bslstl/bslstl_function.cpp"
    "bslstl/bslstl_function.h"
    "bslstl/bslstl_hash.cpp"
    "bslstl/bslstl_hash.h"
    "bslstl/bslstl_hashtable.cpp"
    "bslstl/bslstl_hashtable.h"
    "bslstl/bslstl_hashtablebucketiterator.cpp"
    "bslstl/bslstl_hashtablebucketiterator.h"
    "bslstl/bslstl_hashtableiterator.cpp"
    "bslstl/bslstl_hashtableiterator.h"
    "bslstl/bslstl_iosfwd.cpp"
    "bslstl/bslstl_iosfwd.h"
    "bslstl/bslstl_istringstream.cpp"
    "bslstl/bslstl_istringstream.h"
    "bslstl/bslstl_iterator.cpp"
    "bslstl/bslstl_iterator.h"
    "bslstl/bslstl_iteratorutil.cpp"
    "bslstl/bslstl_iteratorutil.h"
    "bslstl/bslstl_list.cpp"
    "bslstl/bslstl_list.h"
    "bslstl/bslstl_map.cpp"
    "bslstl/bslstl_map.h"
    "bslstl/bslstl_mapcomparator.cpp"
    "bslstl/bslstl_mapcomparator.h"
    "bslstl/bslstl_multimap.cpp"
    "bslstl/bslstl_multimap.h"
    "bslstl/bslstl_multiset.cpp"
    "bslstl/bslstl_multiset.h"
    "bslstl/bslstl_ostringstream.cpp"
    "bslstl/bslstl_ostringstream.h"
    "bslstl/bslstl_ownerless.cpp"
    "bslstl/bslstl_ownerless.h"
    "bslstl/bslstl_pair.cpp"
    "bslstl/bslstl_pair.h"
    "bslstl/bslstl_priorityqueue.cpp"
    "bslstl/bslstl_priorityqueue.h"
    "bslstl/bslstl_queue.cpp"
    "bslstl/bslstl_queue.h"
    "bslstl/bslstl_randomaccessiterator.cpp"
    "bslstl/bslstl_randomaccessiterator.h"
    "bslstl/bslstl_referencewrapper.cpp"
    "bslstl/bslstl_referencewrapper.h"
    "bslstl/bslstl_set.cpp"
    "bslstl/bslstl_set.h"
    "bslstl/bslstl_setcomparator.cpp"
    "bslstl/bslstl_setcomparator.h"
    "bslstl/bslstl_sharedptr.cpp"
    "bslstl/bslstl_sharedptr.h"
    "bslstl/bslstl_sharedptrallocateinplacerep.cpp"
    "bslstl/bslstl_sharedptrallocateinplacerep.h"
    "bslstl/bslstl_sharedptrallocateoutofplacerep.cpp"
    "bslstl/bslstl_sharedptrallocateoutofplacerep.h"
    "bslstl/bslstl_simplepool.cpp"
    "bslstl/bslstl_simplepool.h"
    "bslstl/bslstl_stack.cpp"
    "bslstl/bslstl_stack.h"
    "bslstl/bslstl_stdexceptutil.cpp"
    "bslstl/bslstl_stdexceptutil.h"
    "bslstl/bslstl_string.cpp"
    "bslstl/bslstl_string.h"
    "bslstl/bslstl_stringbuf.cpp"
    "bslstl/bslstl_stringbuf.h"
    "bslstl/bslstl_stringref.cpp"
    "bslstl/bslstl_stringref.h"
    "bslstl/bslstl_stringrefdata.cpp"
    "bslstl/bslstl_stringrefdata.h"
    "bslstl/bslstl_stringstream.cpp"
    "bslstl/bslstl_stringstream.h"
    "bslstl/bslstl_treeiterator.cpp"
    "bslstl/bslstl_treeiterator.h"
    "bslstl/bslstl_treenode.cpp"
    "bslstl/bslstl_treenode.h"
    "bslstl/bslstl_treenodepool.cpp"
    "bslstl/bslstl_treenodepool.h"
    "bslstl/bslstl_unorderedmap.cpp"
    "bslstl/bslstl_unorderedmap.h"
    "bslstl/bslstl_unorderedmapkeyconfiguration.cpp"
    "bslstl/bslstl_unorderedmapkeyconfiguration.h"
    "bslstl/bslstl_unorderedmultimap.cpp"
    "bslstl/bslstl_unorderedmultimap.h"
    "bslstl/bslstl_unorderedmultiset.cpp"
    "bslstl/bslstl_unorderedmultiset.h"
    "bslstl/bslstl_unorderedset.cpp"
    "bslstl/bslstl_unorderedset.h"
    "bslstl/bslstl_unorderedsetkeyconfiguration.cpp"
    "bslstl/bslstl_unorderedsetkeyconfiguration.h"
    "bslstl/bslstl_vector.cpp"
    "bslstl/bslstl_vector.h"
    "bsltf/bsltf_allocargumenttype.cpp"
    "bsltf/bsltf_allocargumenttype.h"
    "bsltf/bsltf_allocbitwisemoveabletesttype.cpp"
    "bsltf/bsltf_allocbitwisemoveabletesttype.h"
    "bsltf/bsltf_allocemplacabletesttype.cpp"
    "bsltf/bsltf_allocemplacabletesttype.h"
    "bsltf/bsltf_alloctesttype.cpp"
    "bsltf/bsltf_alloctesttype.h"
    "bsltf/bsltf_argumenttype.cpp"
    "bsltf/bsltf_argumenttype.h"
    "bsltf/bsltf_bitwisecopyabletesttype.cpp"
    "bsltf/bsltf_bitwisecopyabletesttype.h"
    "bsltf/bsltf_bitwisemoveabletesttype.cpp"
    "bsltf/bsltf_bitwisemoveabletesttype.h"
    "bsltf/bsltf_convertiblevaluewrapper.cpp"
    "bsltf/bsltf_convertiblevaluewrapper.h"
    "bsltf/bsltf_degeneratefunctor.cpp"
    "bsltf/bsltf_degeneratefunctor.h"
    "bsltf/bsltf_emplacabletesttype.cpp"
    "bsltf/bsltf_emplacabletesttype.h"
    "bsltf/bsltf_enumeratedtesttype.cpp"
    "bsltf/bsltf_enumeratedtesttype.h"
    "bsltf/bsltf_evilbooleantype.cpp"
    "bsltf/bsltf_evilbooleantype.h"
    "bsltf/bsltf_movablealloctesttype.cpp"
    "bsltf/bsltf_movablealloctesttype.h"
    "bsltf/bsltf_movabletesttype.cpp"
    "bsltf/bsltf_movabletesttype.h"
    "bsltf/bsltf_moveonlyalloctesttype.cpp"
    "bsltf/bsltf_moveonlyalloctesttype.h"
    "bsltf/bsltf_movestate.cpp"
    "bsltf/bsltf_movestate.h"
    "bsltf/bsltf_nonassignabletesttype.cpp"
    "bsltf/bsltf_nonassignabletesttype.h"
    "bsltf/bsltf_noncopyconstructibletesttype.cpp"
    "bsltf/bsltf_noncopyconstructibletesttype.h"
    "bsltf/bsltf_nondefaultconstructibletesttype.cpp"
    "bsltf/bsltf_nondefaultconstructibletesttype.h"
    "bsltf/bsltf_nonequalcomparabletesttype.cpp"
    "bsltf/bsltf_nonequalcomparabletesttype.h"
    "bsltf/bsltf_nontypicaloverloadstesttype.cpp"
    "bsltf/bsltf_nontypicaloverloadstesttype.h"
    "bsltf/bsltf_simpletesttype.cpp"
    "bsltf/bsltf_simpletesttype.h"
    "bsltf/bsltf_stdalloctesttype.cpp"
    "bsltf/bsltf_stdalloctesttype.h"
    "bsltf/bsltf_stdallocatoradaptor.cpp"
    "bsltf/bsltf_stdallocatoradaptor.h"
    "bsltf/bsltf_stdstatefulallocator.cpp"
    "bsltf/bsltf_stdstatefulallocator.h"
    "bsltf/bsltf_stdtestallocator.cpp"
    "bsltf/bsltf_stdtestallocator.h"
    "bsltf/bsltf_templatetestfacility.cpp"
    "bsltf/bsltf_templatetestfacility.h"
    "bsltf/bsltf_testvaluesarray.cpp"
    "bsltf/bsltf_testvaluesarray.h"
    "bsltf/bsltf_uniontesttype.cpp"
    "bsltf/bsltf_uniontesttype.h"
    "bslx/bslx_byteinstream.cpp"
    "bslx/bslx_byteinstream.h"
    "bslx/bslx_byteoutstream.cpp"
    "bslx/bslx_byteoutstream.h"
    "bslx/bslx_genericinstream.cpp"
    "bslx/bslx_genericinstream.h"
    "bslx/bslx_genericoutstream.cpp"
    "bslx/bslx_genericoutstream.h"
    "bslx/bslx_instreamfunctions.cpp"
    "bslx/bslx_instreamfunctions.h"
    "bslx/bslx_marshallingutil.cpp"
    "bslx/bslx_marshallingutil.h"
    "bslx/bslx_outstreamfunctions.cpp"
    "bslx/bslx_outstreamfunctions.h"
    "bslx/bslx_streambufinstream.cpp"
    "bslx/bslx_streambufinstream.h"
    "bslx/bslx_streambufoutstream.cpp"
    "bslx/bslx_streambufoutstream.h"
    "bslx/bslx_testinstreamexception.cpp"
    "bslx/bslx_testinstreamexception.h"
    "bslx/bslx_testinstream.cpp"
    "bslx/bslx_testinstream.h"
    "bslx/bslx_testoutstream.cpp"
    "bslx/bslx_testoutstream.h"
    "bslx/bslx_typecode.cpp"
    "bslx/bslx_typecode.h"
    "bslx/bslx_versionfunctions.cpp"
    "bslx/bslx_versionfunctions.h"
)
source_group("" FILES ${sources})

add_library(bsl STATIC ${sources})

target_include_directories(bsl PUBLIC
    bsl+bslhdrs
    bsl+stdhdrs
    bslalg
    bsldoc
    bslh
    bslim
    bslma
    bslmf
    bslmt
    bsls
    bslscm
    bslstl
    bsltf
    bslx
)

target_link_libraries(bsl PUBLIC
)
